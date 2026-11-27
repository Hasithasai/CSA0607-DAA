"""Prints a step-by-step event trace of the Version-1 search (used for the A1.5 trace in the report)."""
import itertools, sys
from graph_colouring import build_adj

def trace(n, edges, k, names):
    adj = build_adj(n, edges); colour = [-1] * n; step = [0]
    def log(depth, msg):
        step[0] += 1; print(f"{step[0]:2d}. {'  ' * depth}{msg}")
    def bt(depth):
        if depth == n:
            log(depth, "GOAL: all vertices coloured -> SUCCESS"); return True
        v = colour.index(-1)
        for c in range(k):
            clash = [names[u] for u in adj[v] if colour[u] == c]
            if clash:
                log(depth, f"CHOOSE {names[v]}={c}  CHECK conflict with {clash[0]}  -> REJECT (prune)")
                continue
            log(depth, f"CHOOSE {names[v]}={c}  CHECK ok  -> ACCEPT, EXPLORE")
            colour[v] = c
            if bt(depth + 1): return True
            colour[v] = -1
            log(depth, f"BACKTRACK: undo {names[v]}={c}")
        log(depth, f"no colour left for {names[v]} -> FAIL upward")
        return False
    return bt(0)

if __name__ == "__main__":
    names = ["S1", "S2", "S3", "S4", "S5"]
    # find a 5-vertex graph where input-order search must backtrack yet a 3-colouring exists
    from graph_colouring import colour_graph
    pairs = list(itertools.combinations(range(5), 2))
    best = None
    for mask in range(1 << len(pairs)):
        edges = [p for i, p in enumerate(pairs) if mask >> i & 1]
        if not (6 <= len(edges) <= 7): continue
        col, st = colour_graph(5, edges, 3, "input")
        if col and st.backtracks >= 1 and st.rejected >= 2:
            best = (edges, st); break
    edges, st = best
    print("Graph edges (S1..S5):", [(names[a], names[b]) for a, b in edges], " k = 3")
    trace(5, edges, 3, names)
