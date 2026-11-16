"""Q1: Selection, bubble and insertion sort with operation counters."""
import time

def selection_sort(a):
    a=a.copy(); comparisons=swaps=0
    for i in range(len(a)-1):
        m=i
        for j in range(i+1,len(a)):
            comparisons+=1
            if a[j]<a[m]: m=j
        if m!=i:
            a[i],a[m]=a[m],a[i]; swaps+=1
    return a,comparisons,swaps

def bubble_sort(a):
    a=a.copy(); comparisons=swaps=0
    for end in range(len(a)-1,0,-1):
        changed=False
        for j in range(end):
            comparisons+=1
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]; swaps+=1; changed=True
        if not changed: break
    return a,comparisons,swaps

def insertion_sort(a):
    a=a.copy(); comparisons=moves=0
    for i in range(1,len(a)):
        key=a[i]; j=i-1
        while j>=0:
            comparisons+=1
            if a[j]>key:
                a[j+1]=a[j]; moves+=1; j-=1
            else: break
        a[j+1]=key; moves+=1
    return a,comparisons,moves

def main():
    datasets={
      "Nearly sorted":[1,2,3,5,4,6,7,8,9,10],
      "Reverse ordered":[10,9,8,7,6,5,4,3,2,1],
      "Edge case (duplicates/single value)":[5,5,5,5,5,5,5,5,5,5]
    }
    print("Q1 SORTING EXPERIMENTS")
    for name,data in datasets.items():
        print(f"\n{name}: {data}")
        for label,fn in [("Selection",selection_sort),("Bubble",bubble_sort),("Insertion",insertion_sort)]:
            start=time.perf_counter(); result,c,m=fn(data); elapsed=(time.perf_counter()-start)*1e6
            print(f"{label:10s} sorted={result} comparisons={c:3d} swaps/moves={m:3d} time_us={elapsed:.2f}")
if __name__=="__main__": main()
