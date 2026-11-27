"""
Task B1 - Backtracking graph colouring with full search instrumentation.

Implements the Part A1 pseudocode (COLOUR_GRAPH) in two vertex-selection modes:
  order="input"  : Version 1 - next vertex = lowest-index uncoloured vertex
  order="dsatur" : Version 2 - next vertex = most-constrained uncoloured vertex
                   (largest number of DISTINCT colours already on its neighbours;
                   ties -> more uncoloured neighbours; ties -> lowest index)
"""
from dataclasses import dataclass, field
import sys

sys.setrecursionlimit(10000)


@dataclass
class Stats:
    nodes: int = 0          # search-tree nodes visited (calls of BACKTRACK)
    attempts: int = 0       # candidate (vertex, colour) assignments tried
    rejected: int = 0       # candidates rejected by the feasibility test
    backtracks: int = 0     # undo operations (assignment removed after failed subtree)
    max_depth: int = 0      # deepest level reached (number of coloured vertices)

    def row(self):
        return (self.nodes, self.attempts, self.rejected, self.backtracks, self.max_depth)


def build_adj(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        if u == v:
            raise ValueError("self-loop makes the graph uncolourable; not allowed")
        adj[u].add(v)
        adj[v].add(u)
    return adj


def colour_graph(n, edges, k, order="input"):
    """Return (colouring or None, Stats)."""
    adj = build_adj(n, edges)
    colour = [-1] * n
    st = Stats()

    def select_vertex():
        if order == "input":
            for v in range(n):
                if colour[v] == -1:
                    return v
        else:  # DSATUR-style rule
            best, best_key = None, None
            for v in range(n):
                if colour[v] != -1:
                    continue
                sat = len({colour[u] for u in adj[v] if colour[u] != -1})
                free_deg = sum(1 for u in adj[v] if colour[u] == -1)
                key = (sat, free_deg, -v)
                if best_key is None or key > best_key:
                    best, best_key = v, key
            return best

    def feasible(v, c):
        return all(colour[u] != c for u in adj[v])

    def backtrack(depth):
        st.nodes += 1
        st.max_depth = max(st.max_depth, depth)
        if depth == n:                      # goal: every vertex coloured
            return True
        v = select_vertex()
        for c in range(k):
            st.attempts += 1
            if not feasible(v, c):          # pruning: neighbour already has c
                st.rejected += 1
                continue
            colour[v] = c                   # assign
            if backtrack(depth + 1):        # explore
                return True
            colour[v] = -1                  # undo
            st.backtracks += 1
        return False                        # no colour works -> fail upward

    ok = backtrack(0)
    return (list(colour) if ok else None), st


def is_proper(n, edges, colouring, k):
    return (colouring is not None and len(colouring) == n
            and all(0 <= c < k for c in colouring)
            and all(colouring[u] != colouring[v] for u, v in edges))


# ---------- graph generators used by tests / experiments ----------
def cycle(n):
    return n, [(i, (i + 1) % n) for i in range(n)]

def complete(n):
    return n, [(i, j) for i in range(n) for j in range(i + 1, n)]

def petersen():
    e = [(i, (i + 1) % 5) for i in range(5)]
    e += [(i, i + 5) for i in range(5)]
    e += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return 10, e

def grotzsch():
    """Mycielskian of C5: 11 vertices, triangle-free, chromatic number 4."""
    n, e = cycle(5)
    edges = list(e)
    for u, v in e:
        edges.append((u, 5 + v))
        edges.append((v, 5 + u))
    for i in range(5):
        edges.append((5 + i, 10))
    return 11, edges

def queen_graph(r):
    cells = [(i, j) for i in range(r) for j in range(r)]
    idx = {c: t for t, c in enumerate(cells)}
    edges = []
    for a in range(len(cells)):
        for b in range(a + 1, len(cells)):
            (i1, j1), (i2, j2) = cells[a], cells[b]
            if i1 == i2 or j1 == j2 or abs(i1 - i2) == abs(j1 - j2):
                edges.append((a, b))
    return r * r, edges

def random_graph(n, p, seed):
    import random
    rnd = random.Random(seed)
    return n, [(i, j) for i in range(n) for j in range(i + 1, n) if rnd.random() < p]
