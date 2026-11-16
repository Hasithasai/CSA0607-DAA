"""Q4: Brute-force closest pair of 2D points."""
import math, time, random
def closest_pair(points):
    best=float("inf"); pair=None; examined=0; distances=0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            examined+=1
            dx=points[i][0]-points[j][0]; dy=points[i][1]-points[j][1]
            d2=dx*dx+dy*dy; distances+=1
            if d2<best: best=d2; pair=(points[i],points[j])
    return pair,math.sqrt(best) if pair else None,examined,distances
def main():
    print("Q4 BRUTE-FORCE CLOSEST PAIR")
    random.seed(19)
    for n in (10,100,500,1000):
        pts=[(random.random()*1000,random.random()*1000) for _ in range(n)]
        t=time.perf_counter(); pair,d,pairs,calcs=closest_pair(pts); elapsed=(time.perf_counter()-t)*1000
        expected=n*(n-1)//2
        print(f"n={n:4d} unique_pairs={pairs:8d} expected={expected:8d} distance_calculations={calcs:8d} time_ms={elapsed:.3f} closest_distance={d:.4f}")
if __name__=="__main__": main()
