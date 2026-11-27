"""B1.1 - validation tests. Run:  python3 test_graph_colouring.py"""
import itertools, random
from graph_colouring import *

def brute(n, edges, k):
    for col in itertools.product(range(k), repeat=n):
        if all(col[u] != col[v] for u, v in edges):
            return True
    return False

tests = []
def T(name, n, edges, k, expect, purpose):
    tests.append((name, n, edges, k, expect, purpose))

n, e = cycle(5);  T("Colourable: C5, k=3", n, e, 3, True, "odd cycle needs 3 colours; checks normal success path + valid colouring")
n, e = petersen();T("Colourable: Petersen, k=3", n, e, 3, True, "non-trivial 3-chromatic graph; success needs real backtracking")
n, e = complete(4); T("Uncolourable: K4, k=3", n, e, 3, False, "clique larger than k; must exhaust search and report failure")
n, e = cycle(5);  T("Uncolourable: C5, k=2", n, e, 2, False, "odd cycle is not bipartite; failure only after backtracking")
n, e = grotzsch();T("Uncolourable: Grotzsch, k=3", n, e, 3, False, "triangle-free yet chi=4: failure NOT explained by a clique")
T("Boundary: empty graph (n=0), k=0", 0, [], 0, True, "no vertices -> trivially colourable, empty colouring")
T("Boundary: single vertex, k=0", 1, [], 0, False, "a vertex but no colours -> must fail")
T("Boundary: single vertex, k=1", 1, [], 1, True, "smallest non-trivial success")
T("Boundary: 1 edge, k=1", 2, [(0, 1)], 1, False, "k=1 cannot colour any edge")
T("Boundary: 6 isolated vertices, k=1", 6, [], 1, True, "no edges -> one colour suffices, zero rejections expected")
n, e = complete(5); T("Boundary: K5, k=5 (k = n)", n, e, 5, True, "k equals chromatic number exactly; tight success")
T("Boundary: duplicate edges", 3, [(0,1),(1,0),(1,2),(1,2)], 2, True, "duplicate edges must not break feasibility")

print(f"{'Test':38s}{'Order':8s}{'Expected':10s}{'Got':8s}{'Proper?':9s}Pass")
allok = True
for name, n, edges, k, expect, purpose in tests:
    for order in ("input", "dsatur"):
        col, st = colour_graph(n, edges, k, order)
        got = col is not None
        proper = is_proper(n, edges, col, k) if got else "-"
        ok = (got == expect) and (proper is True or not got)
        allok &= ok
        print(f"{name:38s}{order:8s}{str(expect):10s}{str(got):8s}{str(proper):9s}{'PASS' if ok else 'FAIL'}")
print()
for name, *_rest, purpose in tests:
    print(f"- {name}: {purpose}")

# randomised cross-check against exhaustive enumeration
rnd = random.Random(7); mism = 0; total = 0
for _ in range(300):
    n = rnd.randint(1, 8); p = rnd.choice([0.2, 0.4, 0.6]); k = rnd.randint(1, 4)
    _, edges = random_graph(n, p, rnd.random())
    truth = brute(n, edges, k)
    for order in ("input", "dsatur"):
        col, _ = colour_graph(n, edges, k, order)
        total += 1
        if (col is not None) != truth or (col is not None and not is_proper(n, edges, col, k)):
            mism += 1
print(f"\nRandomised cross-check vs brute force: {total} runs, {mism} mismatches")
print("ALL TESTS PASSED" if allok and mism == 0 else "SOME TESTS FAILED")
