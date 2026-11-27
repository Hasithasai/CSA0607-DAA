"""
Task B3 - Emergency-service Set Cover: exact vs greedy, with operation counts.

Representation: zones = 0..m-1 ; each centre = frozenset of zones it serves.
Bitmasks are used internally so that 'coverage' tests are single integer operations.
"""
from itertools import combinations
from math import comb
import random


def to_masks(m, centres):
    return [sum(1 << z for z in c) for c in centres]


# ---------------------------------------------------------------- exact (a): brute force
def exact_bruteforce(m, centres):
    """Try every combination of size 1,2,3,... ; first size that covers all zones is optimal.
    effort = number of combinations tested."""
    masks = to_masks(m, centres); full = (1 << m) - 1; tested = 0
    for size in range(1, len(centres) + 1):
        for combo in combinations(range(len(centres)), size):
            tested += 1
            cov = 0
            for i in combo:
                cov |= masks[i]
            if cov == full:
                return list(combo), tested
    return None, tested


# ---------------------------------------------------------------- exact (b): branch & bound
def exact_bnb(m, centres):
    """Exact search with pruning.  Branch on the uncovered zone that has the fewest candidate centres
    (one of them MUST be chosen), prune when |chosen| + lower bound >= best.
    effort = number of search states (calls)."""
    masks = to_masks(m, centres); full = (1 << m) - 1
    covering = [[i for i, mk in enumerate(masks) if mk >> z & 1] for z in range(m)]
    max_cover = max(bin(mk).count("1") for mk in masks)
    best = [len(centres) + 1, None]; states = [0]

    def rec(cov, chosen):
        states[0] += 1
        if cov == full:
            if len(chosen) < best[0]:
                best[0], best[1] = len(chosen), list(chosen)
            return
        remaining = m - bin(cov).count("1")
        lb = -(-remaining // max_cover)               # ceil(remaining / largest set)
        if len(chosen) + lb >= best[0]:               # PRUNE: cannot beat incumbent
            return
        # most constrained uncovered zone
        zbest, opts = None, None
        for z in range(m):
            if not (cov >> z & 1):
                c = covering[z]
                if opts is None or len(c) < len(opts):
                    zbest, opts = z, c
        for i in sorted(opts, key=lambda i: -bin(masks[i] & ~cov).count("1")):
            chosen.append(i); rec(cov | masks[i], chosen); chosen.pop()

    rec(0, [])
    return best[1], states[0]


# ---------------------------------------------------------------- greedy approximation
def greedy(m, centres, trace=False):
    """effort = number of (centre, uncovered-zone-count) evaluations = selection-criterion evaluations."""
    masks = to_masks(m, centres); uncovered = (1 << m) - 1
    selected, evals, log = [], 0, []
    while uncovered:
        best_i, best_gain = -1, 0
        for i, mk in enumerate(masks):
            evals += 1
            gain = bin(mk & uncovered).count("1")
            if gain > best_gain:                         # first maximum wins ties (lowest index)
                best_i, best_gain = i, gain
        if best_i == -1:
            return None, evals, log                      # some zone is uncoverable
        selected.append(best_i)
        uncovered &= ~masks[best_i]
        log.append((best_i, best_gain, bin(uncovered).count("1")))
    return selected, evals, log


def valid_cover(m, centres, chosen):
    return set().union(*[centres[i] for i in chosen]) == set(range(m)) if chosen else m == 0


def random_instance(m, n, seed, density=0.18):
    rnd = random.Random(seed)
    centres = [frozenset(z for z in range(m) if rnd.random() < density) for _ in range(n)]
    for z in range(m):                                   # make sure every zone is coverable
        if not any(z in c for c in centres):
            centres[rnd.randrange(n)] |= {z}
    centres = [c if c else frozenset([rnd.randrange(m)]) for c in centres]
    return m, centres
