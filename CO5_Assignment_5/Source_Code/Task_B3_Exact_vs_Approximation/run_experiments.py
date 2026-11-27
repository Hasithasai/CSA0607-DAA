import time
from math import comb
from set_cover import *

def show(c): return "{" + ",".join(str(z + 1) for z in sorted(c)) + "}"

print("=" * 78); print("B3.1  CORRECTNESS ON SMALL INSTANCES (zones numbered 1..m in the printout)")
print("=" * 78)
inst = {}
# Instance 1: deliberately simple
inst[1] = (6, [frozenset(s) for s in ({0,1,2},{3,4,5},{0,3},{1,4},{2,5})])
# Instance 2: random-looking, drawn without checking whether greedy would match
inst[2] = random_instance(10, 8, seed=2)
# Instance 3: random, different seed
inst[3] = random_instance(12, 9, seed=9)
# Instance 4 & 5: more random draws, reported regardless of the outcome
inst[4] = random_instance(14, 10, seed=21)
inst[5] = random_instance(15, 11, seed=33)
print(f"{'Inst':5s}{'zones':>6s}{'centres':>8s}{'Exact(brute)':>14s}{'Exact(B&B)':>12s}{'Greedy':>8s}{'Same?':>7s}")
for k, (m, cs) in inst.items():
    eb, _ = exact_bruteforce(m, cs); ex, _ = exact_bnb(m, cs); g, _, _ = greedy(m, cs)
    assert len(eb) == len(ex) and valid_cover(m, cs, eb) and valid_cover(m, cs, g)
    print(f"{k:<5d}{m:6d}{len(cs):8d}{len(eb):14d}{len(ex):12d}{len(g):8d}{('YES' if len(g)==len(eb) else 'NO'):>7s}")
print("\nInstance 1 centres:", [show(c) for c in inst[1][1]])

print("\n" + "=" * 78); print("B3.2  COUNTEREXAMPLE FOR GREEDY"); print("=" * 78)
m = 12
cs = [frozenset(range(0, 6)),            # S0 = {1..6}
      frozenset(range(6, 12)),           # S1 = {7..12}
      frozenset([0,1,2,3,6,7,8,9]),      # S2 = {1,2,3,4,7,8,9,10}  <- the 'attractive' trap
      frozenset([4, 5]),                 # S3 = {5,6}
      frozenset([10, 11])]               # S4 = {11,12}
for i, c in enumerate(cs): print(f"  S{i} = {show(c)}")
ex, _ = exact_bruteforce(m, cs); g, ev, log = greedy(m, cs)
print("Exact optimum :", [f"S{i}" for i in ex], "size", len(ex))
print("Greedy picks  :", [f"S{i}" for i in g], "size", len(g))
for step, (i, gain, left) in enumerate(log, 1):
    print(f"   step {step}: choose S{i} (covers {gain} new zones) -> {left} zones still uncovered")

print("\n" + "=" * 78); print("B3.3  SCALABILITY"); print("=" * 78)
print("Exact effort = states visited by branch&bound (and #combinations a plain brute-force would test up to the optimum size)")
print("Greedy effort = number of centre-gain evaluations")
hdr = f"{'zones':>6s}{'centres':>8s}{'Exact B&B states':>18s}{'Brute-force combos':>20s}{'Greedy evals':>14s}{'Exact':>7s}{'Greedy':>8s}{'B&B s':>9s}{'Greedy s':>10s}"
print(hdr); print("-" * len(hdr))
for (m, n, seed) in [(12,10,1),(20,15,2),(30,20,3),(40,28,4),(50,35,5),(60,42,6),(80,60,7)]:
    mm, cs = random_instance(m, n, seed, density=0.12)
    t = time.perf_counter(); ex, states = exact_bnb(mm, cs); t1 = time.perf_counter() - t
    t = time.perf_counter(); g, ev, _ = greedy(mm, cs); t2 = time.perf_counter() - t
    opt = len(ex)
    brute = sum(comb(n, j) for j in range(1, opt + 1))
    print(f"{m:6d}{n:8d}{states:18d}{brute:20d}{ev:14d}{opt:7d}{len(g):8d}{t1:9.4f}{t2:10.5f}")

print("\nDoubling test: brute-force combinations needed as #centres grows (optimum size 6 assumed):")
for n in (20, 30, 40, 60, 80, 100):
    print(f"  n={n:3d}  sum_(j<=6) C(n,j) = {sum(comb(n,j) for j in range(1,7)):,}")
