"""Q7: Redesign Q6 using 0/1 dynamic programming."""
import time
def exhaustive(items,capacity):
    n=len(items); best=-1; bestmask=0; examined=0
    for mask in range(1<<n):
        examined+=1; w=v=0
        for i,(wi,vi) in enumerate(items):
            if mask>>i&1: w+=wi; v+=vi
        if w<=capacity and v>best: best=v; bestmask=mask
    return best,examined
def dynamic_programming(items,capacity):
    # dp[c] = best value achievable with capacity at most c after processed items.
    dp=[0]*(capacity+1); updates=0
    for weight,value in items:
        for c in range(capacity,weight-1,-1):
            candidate=dp[c-weight]+value; updates+=1
            if candidate>dp[c]: dp[c]=candidate
    return dp[capacity],updates
def main():
    print("Q7 DAY-4 DESIGN CHALLENGE: EXHAUSTIVE SEARCH vs DYNAMIC PROGRAMMING")
    capacity=60
    for n in (10,15,20):
        items=[(2+(i*7)%13, 4+(i*11)%25) for i in range(n)]
        t=time.perf_counter(); a,subsets=exhaustive(items,capacity); te=(time.perf_counter()-t)*1000
        t=time.perf_counter(); b,updates=dynamic_programming(items,capacity); td=(time.perf_counter()-t)*1000
        print(f"n={n:2d} exhaustive_subsets={subsets:8d} DP_state_updates={updates:6d} values={a}/{b} times_ms={te:.3f}/{td:.3f} verified={a==b}")
if __name__=="__main__": main()
