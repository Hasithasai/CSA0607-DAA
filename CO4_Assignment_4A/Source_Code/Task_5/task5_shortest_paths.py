"""Task 5 - Dijkstra, Bellman-Ford and Floyd-Warshall on the same graph."""
INF = float("inf")

def dijkstra(V, E, src):
    dist = {v: INF for v in V}; pred = {v: None for v in V}; dist[src] = 0
    done = set(); adj = {v: [] for v in V}
    for u, v, w in E: adj[u].append((v, w))
    while len(done) < len(V):
        cand = [v for v in V if v not in done and dist[v] < INF]
        if not cand: break
        u = min(cand, key=lambda v: dist[v])          # EXTRACT_MIN
        done.add(u)
        print(f"  finalise {u} (dist={dist[u]})")
        for v, w in adj[u]:
            if v not in done and dist[u] + w < dist[v]:   # relaxation
                dist[v] = dist[u] + w; pred[v] = u
                print(f"     relax {u}->{v} (w={w}): dist[{v}]={dist[v]}, pred[{v}]={u}")
    return dist, pred

def bellman_ford(V, E, src):
    dist = {v: INF for v in V}; pred = {v: None for v in V}; dist[src] = 0
    for k in range(1, len(V)):
        changed = False
        for u, v, w in E:
            if dist[u] < INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; pred[v] = u; changed = True
        print(f"  pass {k}: {dist}")
        if not changed: break
    cycle = any(dist[u] < INF and dist[u] + w < dist[v] for u, v, w in E)   # V-th pass
    return dist, pred, cycle

def floyd(V, E):
    idx = {v: i for i, v in enumerate(V)}; n = len(V)
    D = [[INF] * n for _ in range(n)]
    for i in range(n): D[i][i] = 0
    for u, v, w in E: D[idx[u]][idx[v]] = min(D[idx[u]][idx[v]], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D

def path(pred, t):
    p = []
    while t is not None: p.append(t); t = pred[t]
    return "->".join(reversed(p))

if __name__ == "__main__":
    V = list("ABCDE")
    E = [("A","B",4),("A","C",7),("B","C",2),("B","D",6),("C","D",1),("D","E",3),("C","E",8)]
    print("=== 5.1 Dijkstra from A ===")
    d, p = dijkstra(V, E, "A")
    for v in V: print(f"  {v}: dist={d[v]} path={path(p, v)}")
    assert d == {"A":0,"B":4,"C":6,"D":7,"E":10}
    print("\n=== 5.2 Bellman-Ford on the same graph ===")
    d2, p2, cyc = bellman_ford(V, E, "A"); print("  final:", d2, "| negative cycle:", cyc); assert d2 == d and not cyc
    print("\n--- Negative edge where Dijkstra is unsafe: A->B 3, A->C 5, C->B -4, B->D 1 ---")
    V2 = list("ABCD"); E2 = [("A","B",3),("A","C",5),("C","B",-4),("B","D",1)]
    dd, _ = dijkstra(V2, E2, "A"); print("  Dijkstra   :", dd)
    bd, _, c2 = bellman_ford(V2, E2, "A"); print("  Bellman-Ford:", bd, "| negative cycle:", c2)
    assert dd["B"] == 3 and bd["B"] == 1
    print("\n--- Negative cycle: A->B 1, B->C -2, C->B 1 ---")
    V3 = list("ABC"); E3 = [("A","B",1),("B","C",-2),("C","B",1)]
    _, _, c3 = bellman_ford(V3, E3, "A"); print("  negative cycle detected:", c3); assert c3
    print("\n=== 5.3 Floyd-Warshall all pairs ===")
    D = floyd(V, E)
    print("     " + "".join(f"{v:>5}" for v in V))
    for i, v in enumerate(V): print(f"  {v}: " + "".join(f"{('INF' if x==INF else x):>5}" for x in D[i]))
    assert D[0][4] == 10
    print("All Task 5 tests passed.")
