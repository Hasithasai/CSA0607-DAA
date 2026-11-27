"""Task 3 - 0/1 Knapsack by dynamic programming with item reconstruction."""

def knapsack(items, W, verbose=True):
    n = len(items)
    K = [[0] * (W + 1) for _ in range(n + 1)]          # K[i][w]: best value using first i items, capacity w
    for i in range(1, n + 1):                           # increasing i: row i-1 is complete
        _, wt, val = items[i - 1]
        for w in range(0, W + 1):
            K[i][w] = K[i - 1][w]                       # exclude
            if wt <= w and val + K[i - 1][w - wt] > K[i][w]:
                K[i][w] = val + K[i - 1][w - wt]        # include
    chosen, w = [], W
    for i in range(n, 0, -1):                           # reconstruction
        if K[i][w] != K[i - 1][w]:
            chosen.append(items[i - 1][0]); w -= items[i - 1][1]
    chosen.reverse()
    if verbose:
        print("w     " + " ".join(f"{x:3d}" for x in range(W + 1)))
        for i in range(n + 1):
            lab = "i=0 " if i == 0 else f"i={i} ({items[i-1][0]})"
            print(f"{lab:6s}" + " ".join(f"{K[i][x]:3d}" for x in range(W + 1)))
    return K[n][W], chosen, K

if __name__ == "__main__":
    items = [("P", 2, 12), ("Q", 3, 20), ("R", 4, 25), ("S", 5, 30)]
    best, chosen, K = knapsack(items, 7)
    print("Optimum value =", best, "| items selected =", chosen)
    w = 7
    print("Reconstruction trace:")
    for i in range(4, 0, -1):
        inc = K[i][w] != K[i-1][w]
        print(f"  i={i} ({items[i-1][0]}), w={w}: K[{i}][{w}]={K[i][w]} vs K[{i-1}][{w}]={K[i-1][w]} -> {'INCLUDE' if inc else 'exclude'}")
        if inc: w -= items[i-1][1]
    assert best == 45 and chosen == ["Q", "R"]
    from itertools import combinations
    bf = max(sum(x[2] for x in c) for r in range(5) for c in combinations(items, r) if sum(x[1] for x in c) <= 7)
    assert bf == best
    print("Brute-force check agrees:", bf)
    print("Boundary: capacity 0 ->", knapsack(items, 0, False)[:2], "| capacity 1 ->", knapsack(items, 1, False)[:2])
    print("All Task 3 tests passed.")
