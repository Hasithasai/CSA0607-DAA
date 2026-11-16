"""Q6: Exhaustive subset search for humanitarian package loading."""
import time
def exhaustive_knapsack(items, capacity):
    n=len(items); best_value=-1; best_mask=0; feasible=0
    for mask in range(1<<n):
        weight=value=0
        for i,(w,v) in enumerate(items):
            if mask & (1<<i): weight+=w; value+=v
        if weight<=capacity:
            feasible+=1
            if value>best_value: best_value=value; best_mask=mask
    chosen=[i+1 for i in range(n) if best_mask&(1<<i)]
    weight=sum(items[i-1][0] for i in chosen)
    return chosen,weight,best_value,(1<<n),feasible
def main():
    print("Q6 EXHAUSTIVE SEARCH (0/1 KNAPSACK)")
    capacity=30
    for n in (8,12,16,20):
        items=[(3+(i*7)%11, 5+(i*13)%23) for i in range(n)]
        t=time.perf_counter(); chosen,w,v,candidates,feasible=exhaustive_knapsack(items,capacity); ms=(time.perf_counter()-t)*1000
        print(f"n={n:2d} candidates={candidates:8d} feasible={feasible:8d} best_value={v:4d} weight={w:3d} time_ms={ms:.3f}")
    small=[(2,3),(3,4),(4,5),(5,8)]
    print("Manual-check instance:",exhaustive_knapsack(small,8)[:3], "capacity=8")
if __name__=="__main__": main()
