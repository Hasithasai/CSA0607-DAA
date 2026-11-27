import random, time
from bin_packing import *

CAP = 100
print("=" * 78); print("B4.1  ALLOCATION OUTPUT (FFD), 12 workloads, capacity 100"); print("=" * 78)
demo = list(enumerate([45, 70, 30, 25, 55, 20, 15, 60, 35, 10, 40, 5], 1))
servers, comps = first_fit(demo, CAP)
report(servers, CAP)
print("Lower bound ceil(sum/C) =", lower_bound(demo, CAP), "| exact optimum =", exact_min_bins([d for _, d in demo], CAP)[0])
assert all(s["free"] >= 0 for s in servers) and sum(len(s["load"]) for s in servers) == len(demo)

print("\n" + "=" * 78); print("B4.2  CHALLENGE: inputs where the heuristics use MORE servers than optimal"); print("=" * 78)
# (a) hand-built, capacity 100 : classic FFD failure
rnd = random.Random(0); found = None
for _ in range(200000):
    n = rnd.randint(6, 10)
    dem = [rnd.randint(10, 50) for _ in range(n)]
    its = list(enumerate(dem, 1))
    s, _ = first_fit(its, CAP)
    opt, _ = exact_min_bins(dem, CAP)
    if len(s) > opt:
        found = (dem, len(s), opt, s); break
dem, nffd, opt, s = found
print("Random search (seed 0) found a counterexample for FFD:")
print("  demands:", dem, "sum =", sum(dem))
print("  FFD uses", nffd, "servers, exact optimum =", opt, ", lower bound =", lower_bound(list(enumerate(dem)), CAP))
report(s, CAP)
# optimal packing, found by brute force assignment
import itertools
def find_packing(dem, k):
    n = len(dem)
    def rec(i, bins, asg):
        if i == n: return list(asg)
        seen = set()
        for b in range(k):
            if bins[b] + dem[i] <= CAP and bins[b] not in seen:
                seen.add(bins[b]); bins[b] += dem[i]; asg.append(b)
                r = rec(i + 1, bins, asg)
                if r: return r
                asg.pop(); bins[b] -= dem[i]
        return None
    return rec(0, [0] * k, [])
asg = find_packing(sorted(dem, reverse=True), opt)
print("  An optimal packing (sorted demands -> server index):")
for b in range(opt):
    print(f"    Server {b+1}: {[d for d, a in zip(sorted(dem, reverse=True), asg) if a == b]}")
# online First-Fit also (arrival order)
ff = [(i + 1, d) for i, d in enumerate([30, 30, 30, 70, 70, 70])]
s_ff, _ = first_fit(ff, CAP, decreasing=False); s_fd, _ = first_fit(ff, CAP, decreasing=True)
print("\nSecond example (arrival order matters): demands [30,30,30,70,70,70], capacity 100")
print("  First-Fit in arrival order uses", len(s_ff), "servers; FFD uses", len(s_fd), "; optimum = 3")

# frequency of failure
bad = tot = 0; worst = 0
rnd = random.Random(1)
for _ in range(3000):
    n = rnd.randint(6, 12); dem = [rnd.randint(5, 60) for _ in range(n)]
    s, _ = first_fit(list(enumerate(dem)), CAP); o, _ = exact_min_bins(dem, CAP)
    tot += 1; bad += len(s) > o; worst = max(worst, len(s) - o)
print(f"\nRandom small inputs (n=6..12): FFD optimal in {tot-bad}/{tot} cases; worst gap = {worst} server(s)")

print("\n" + "=" * 78); print("B4.3  SCALE EVIDENCE (workloads uniform in [5,60], capacity 100, seed fixed)"); print("=" * 78)
print(f"{'N':>8s}{'FFD servers':>13s}{'FF(arrival)':>13s}{'LowerBound':>12s}{'FFD/LB':>8s}{'FFD comps':>14s}{'N^2/2':>14s}{'FFD time s':>12s}")
for N in (100, 1000, 5000, 20000):
    rnd = random.Random(42)
    items = [(i, rnd.randint(5, 60)) for i in range(N)]
    t = time.perf_counter(); sv, c = first_fit(items, CAP); dt = time.perf_counter() - t
    sv2, _ = first_fit(items, CAP, decreasing=False)
    lb = lower_bound(items, CAP)
    print(f"{N:8d}{len(sv):13d}{len(sv2):13d}{lb:12d}{len(sv)/lb:8.3f}{c:14d}{N*N//2:14d}{dt:12.4f}")
print("\nExact-search growth on small inputs (nodes of branch&bound, random demands in [26,49]):")
for n in (8, 12, 16, 20, 24):
    rnd = random.Random(n); dem = [rnd.randint(26, 49) for _ in range(n)]
    t = time.perf_counter(); o, nd = exact_min_bins(dem, CAP); dt = time.perf_counter() - t
    print(f"  n={n:2d}  optimum={o:2d}  nodes={nd:10d}  time={dt:.3f}s")
