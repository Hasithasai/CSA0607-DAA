"""Task 6 - Energy-aware job scheduling = weighted interval scheduling (dynamic programming)."""
from bisect import bisect_right
from itertools import combinations

def schedule(jobs, verbose=True):
    # jobs: (id, start, finish, value). Sort by finish time.
    J = sorted(jobs, key=lambda j: j[2]); n = len(J)
    fin = [j[2] for j in J]
    p = [0] * (n + 1)          # p[k]: count of earlier jobs (finish order) finishing <= start of job k
    for k in range(1, n + 1):
        p[k] = bisect_right(fin, J[k - 1][1], 0, k - 1)
    OPT = [0] * (n + 1); take = [False] * (n + 1)
    if verbose: print(f"{'k':>2} {'job':>4} {'s':>3} {'f':>3} {'v':>4} {'p(k)':>5} {'excl':>5} {'incl':>5} {'OPT':>5}  decision")
    for k in range(1, n + 1):
        jid, s, f, v = J[k - 1]
        excl, incl = OPT[k - 1], v + OPT[p[k]]
        if incl > excl: OPT[k] = incl; take[k] = True
        else: OPT[k] = excl
        if verbose: print(f"{k:>2} {jid:>4} {s:>3} {f:>3} {v:>4} {p[k]:>5} {excl:>5} {incl:>5} {OPT[k]:>5}  {'INCLUDE' if take[k] else 'exclude'}")
    sel, k = [], n
    while k > 0:
        if take[k]: sel.append(J[k - 1]); k = p[k]
        else: k -= 1
    sel.reverse()
    return OPT[n], sel

def greedy(jobs, key):
    chosen = []
    for j in sorted(jobs, key=key):
        if all(j[2] <= c[1] or c[2] <= j[1] for c in chosen): chosen.append(j)
    return sum(c[3] for c in chosen), [c[0] for c in chosen]

def brute(jobs):
    best = 0
    for r in range(len(jobs) + 1):
        for c in combinations(jobs, r):
            c = sorted(c, key=lambda j: j[2])
            if all(c[i][2] <= c[i + 1][1] for i in range(len(c) - 1)):
                best = max(best, sum(j[3] for j in c))
    return best

if __name__ == "__main__":
    jobs = [("J1",1,3,20),("J2",2,5,50),("J3",4,6,30),("J4",6,8,40),("J5",5,9,60),("J6",8,10,30),("J7",9,11,50),("J8",11,13,40)]
    print("=== Given dataset (DP) ===")
    best, sel = schedule(jobs)
    print("Selected:", [j[0] for j in sel], "| total energy saving =", best)
    assert best == 200 and [j[0] for j in sel] == ["J2","J5","J7","J8"] and brute(jobs) == 200
    print("Greedy (highest value):", greedy(jobs, lambda j: -j[3]))
    print("Greedy (earliest finish):", greedy(jobs, lambda j: j[2]))

    print("\n=== Adversarial dataset (Stage 6) ===")
    adv = [("S1",4,5,20),("S2",4,9,40),("S3",9,10,60),("S4",11,12,10),("S5",4,12,30),("S6",3,12,90)]
    print("Greedy (highest value):  ", greedy(adv, lambda j: -j[3]))
    print("Greedy (earliest finish):", greedy(adv, lambda j: j[2]))
    best, sel = schedule(adv)
    print("DP selected:", [j[0] for j in sel], "| total =", best, "| brute force =", brute(adv))
    assert best == brute(adv) == 110

    print("\n=== Touching intervals & ties ===")
    t = [("T1",1,2,5),("T2",2,3,5),("T3",3,4,5)]
    b, s = schedule(t, False); print("Chain of touching jobs ->", b, [j[0] for j in s]); assert b == 15
    t = [("U1",1,5,10),("U2",1,5,10)]
    b, s = schedule(t, False); print("Identical overlapping jobs ->", b, [j[0] for j in s]); assert b == 10
    print("\nAll Task 6 tests passed.")
