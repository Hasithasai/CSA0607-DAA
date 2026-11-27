"""
Task B4 - Workload placement (bin packing).

Placement rule used (First-Fit Decreasing, FFD):
  1. sort workloads by demand, largest first
  2. place each workload on the FIRST server whose remaining capacity >= demand
  3. if none fits, open a new server
Also implemented for comparison: First-Fit (arrival order, i.e. fully online) and an exact solver for small inputs.
"""
import math, random, time


def first_fit(items, cap, decreasing=True):
    """items: list of (workload_id, demand). Returns (servers, comparisons)."""
    order = sorted(items, key=lambda x: -x[1]) if decreasing else list(items)
    servers = []          # each: {"load": [...], "free": remaining}
    comps = 0
    for wid, d in order:
        if not (0 < d <= cap):
            raise ValueError(f"workload {wid} demand {d} outside (0, {cap}]")
        placed = False
        for s in servers:
            comps += 1
            if s["free"] >= d:                      # feasibility test
                s["load"].append((wid, d)); s["free"] -= d
                placed = True; break
        if not placed:
            servers.append({"load": [(wid, d)], "free": cap - d})
    return servers, comps


def lower_bound(items, cap):
    return math.ceil(sum(d for _, d in items) / cap)


def exact_min_bins(demands, cap):
    """Exact branch & bound for small inputs. Returns (min bins, nodes)."""
    d = sorted(demands, reverse=True)
    best = [len(d)]; nodes = [0]
    lb0 = math.ceil(sum(d) / cap)

    def rec(i, bins):
        nodes[0] += 1
        if len(bins) >= best[0]:
            return
        if i == len(d):
            best[0] = len(bins); return
        if best[0] == lb0:
            return
        seen = set()
        for b in range(len(bins)):
            if bins[b] + d[i] <= cap and bins[b] not in seen:
                seen.add(bins[b]); bins[b] += d[i]; rec(i + 1, bins); bins[b] -= d[i]
        bins.append(d[i]); rec(i + 1, bins); bins.pop()
    rec(0, [])
    return best[0], nodes[0]


def report(servers, cap, limit=None):
    print(f"Servers used: {len(servers)}  (capacity each = {cap})")
    for i, s in enumerate(servers[:limit]):
        ids = ", ".join(f"w{w}:{d}" for w, d in s["load"])
        print(f"  Server {i+1:3d}: [{ids}]  used={cap - s['free']}  remaining={s['free']}")
    if limit and len(servers) > limit:
        print(f"  ... {len(servers) - limit} more servers")
