"""B1.3 / B1.4 - Version 1 (input order) vs Version 2 (DSATUR-style order)."""
from graph_colouring import *

# For the 'input order' to be fair we use the labelling as generated (not adversarially permuted).
cases = [
    ("C5, k=3",                 *cycle(5),            3),
    ("Petersen, k=3",           *petersen(),          3),
    ("Grotzsch, k=3 (no sol.)", *grotzsch(),          3),
    ("Queen5x5, k=5",           *queen_graph(5),      5),
    ("Queen5x5, k=4 (no sol.)", *queen_graph(5),      4),
    ("Random G(18,.35), k=4",   *random_graph(18, .35, 11), 4),
    ("Random G(22,.30), k=3",   *random_graph(22, .30, 5),  3),
    ("Random G(25,.25), k=3",   *random_graph(25, .25, 3),  3),
]
hdr = f"{'Instance':26s}{'V':3s}{'Result':8s}{'Nodes':>9s}{'Attempts':>10s}{'Rejected':>10s}{'Backtr.':>9s}{'MaxDep':>7s}"
print(hdr); print("-" * len(hdr))
for name, n, edges, k in cases:
    for tag, order in (("1", "input"), ("2", "dsatur")):
        col, st = colour_graph(n, edges, k, order)
        assert col is None or is_proper(n, edges, col, k)
        print(f"{name:26s}{tag:3s}{('colour' if col else 'none'):8s}{st.nodes:9d}{st.attempts:10d}{st.rejected:10d}{st.backtracks:9d}{st.max_depth:7d}")
    print()

print("Example final colouring (Petersen, k=3, Version 2):")
n, e = petersen(); col, st = colour_graph(n, e, 3, "dsatur"); print(col)
print("Example final colouring (Petersen, k=3, Version 1):")
col, st = colour_graph(n, e, 3, "input"); print(col)
