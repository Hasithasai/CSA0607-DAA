"""Task 2 - Job Sequencing with Deadlines (greedy: highest profit first, latest free slot)."""

def job_sequencing(jobs, verbose=True):
    # jobs: list of (id, deadline, profit)
    order = sorted(jobs, key=lambda j: j[2], reverse=True)
    max_d = max(j[1] for j in jobs)
    slot = [None] * (max_d + 1)                  # slot[1..max_d]
    total = 0
    if verbose:
        print("Order by profit:", [(j[0], j[2]) for j in order], "| max deadline =", max_d)
    for jid, d, p in order:
        t = min(d, max_d)
        while t >= 1 and slot[t] is not None:    # search latest free slot <= deadline
            t -= 1
        if t >= 1:
            slot[t] = jid
            total += p
            if verbose: print(f"  {jid}(d={d},p={p}): placed in slot {t} -> slots={slot[1:]} profit={total}")
        elif verbose:
            print(f"  {jid}(d={d},p={p}): no free slot <= {d}, REJECTED -> slots={slot[1:]} profit={total}")
    return slot[1:], total

if __name__ == "__main__":
    base = [("A", 2, 80), ("B", 1, 35), ("C", 2, 60), ("D", 3, 40), ("E", 1, 25)]
    print("=== Desk-check instance ===")
    s, t = job_sequencing(base); print("Schedule:", s, "Total profit:", t); assert t == 180
    print("\n=== Challenge: profit of B changed 35 -> 90 ===")
    mod = [("A", 2, 80), ("B", 1, 90), ("C", 2, 60), ("D", 3, 40), ("E", 1, 25)]
    s, t = job_sequencing(mod); print("Schedule:", s, "Total profit:", t); assert t == 210
    print("\n=== Boundary: all jobs have deadline 1 ===")
    s, t = job_sequencing([("X", 1, 10), ("Y", 1, 50), ("Z", 1, 30)]); print("Schedule:", s, "Total profit:", t); assert t == 50
    print("\nAll Task 2 tests passed.")
