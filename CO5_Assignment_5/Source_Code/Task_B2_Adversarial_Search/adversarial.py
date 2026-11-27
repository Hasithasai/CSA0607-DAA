"""
B2 - Same size, very different search.   n = 14 vertices, k = 3 colours, in BOTH graphs.

Both graphs contain exactly the same ingredients:
   * one K4 (4 mutually conflicting services)  -> NOT 3-colourable (every run must fail)
   * 10 'filler' vertices joined by 5 disjoint edges (loosely constrained, many valid colourings)
   * the same number of edges (6 + 5 = 11)

Graph A : K4 is on vertices 0-3 (first in input order)    -> conflict exposed at depth 4
Graph B : K4 is on vertices 10-13 (last in input order)   -> 10 loose vertices are coloured first,
          every one of their (6^5 = 7776) valid colourings is explored and then refuted.
"""
from graph_colouring import *

K4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
FILLER = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]          # 5 disjoint edges on 10 vertices

def graph_A():
    edges = [(u, v) for u, v in K4] + [(4 + a, 4 + b) for a, b in FILLER]
    return 14, edges

def graph_B():
    edges = [(a, b) for a, b in FILLER] + [(10 + u, 10 + v) for u, v in K4]
    return 14, edges

def run(name, n, edges, k=3):
    print(f"{name}: n={n}, |E|={len(edges)}, k={k}")
    for tag, order in (("Version 1 (input order)", "input"), ("Version 2 (DSATUR order)", "dsatur")):
        col, st = colour_graph(n, edges, k, order)
        print(f"   {tag:26s} result={'colourable' if col else 'NOT colourable':15s} "
              f"nodes={st.nodes:8d} backtracks={st.backtracks:8d} rejected={st.rejected:8d} "
              f"attempts={st.attempts:8d} max_depth={st.max_depth}")
    print()

if __name__ == "__main__":
    nA, eA = graph_A(); nB, eB = graph_B()
    print("Edges A:", eA); print("Edges B:", eB); print()
    run("Graph A (K4 first)", nA, eA)
    run("Graph B (K4 last)", nB, eB)
    # Scaling the gap: more loose filler edges -> exponential growth under input order
    print("Growth of Version-1 effort for Graph B as the filler grows (k=3, K4 last):")
    print(f"{'filler edges':>13s}{'n':>5s}{'nodes (V1)':>14s}{'nodes (V2)':>14s}")
    for m in range(1, 8):
        filler = [(2 * i, 2 * i + 1) for i in range(m)]
        n = 2 * m + 4
        edges = filler + [(2 * m + u, 2 * m + v) for u, v in K4]
        _, s1 = colour_graph(n, edges, 3, "input")
        _, s2 = colour_graph(n, edges, 3, "dsatur")
        print(f"{m:13d}{n:5d}{s1.nodes:14d}{s2.nodes:14d}")
