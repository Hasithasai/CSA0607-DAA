"""Q5: Brute-force convex hull by checking all point pairs."""
import itertools
def cross(a,b,p):
    return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
def convex_hull(points):
    pts=list(dict.fromkeys(points)); n=len(pts); edges=[]; tests=0
    if n<2: return pts,edges,tests
    for i,j in itertools.combinations(range(n),2):
        pos=neg=False
        for k,p in enumerate(pts):
            if k in (i,j): continue
            tests+=1; z=cross(pts[i],pts[j],p)
            if z>0: pos=True
            elif z<0: neg=True
            if pos and neg: break
        if not (pos and neg): edges.append((pts[i],pts[j]))
    # For plotting/order, monotone chain is used only to order the accepted boundary vertices.
    # Edge acceptance itself is the brute-force all-points-one-side test above.
    ordered=sorted(set(p for e in edges for p in e))
    if len(ordered)<=1: return ordered,edges,tests
    def half(seq):
        out=[]
        for p in seq:
            while len(out)>=2 and cross(out[-2],out[-1],p)<=0: out.pop()
            out.append(p)
        return out
    hull=half(ordered)+half(ordered[::-1])[1:-1]
    return hull,edges,tests
def main():
    cases={
      "Interior points":[(0,0),(4,0),(4,4),(0,4),(2,2),(1,2),(3,1)],
      "Collinear challenge":[(0,0),(1,1),(2,2),(3,3),(0,3),(3,0),(1,2),(2,1)],
      "Triangle plus interior":[(0,0),(6,0),(3,5),(3,2),(2,1),(4,1)]
    }
    print("Q5 BRUTE-FORCE CONVEX HULL")
    for name,pts in cases.items():
        hull,edges,tests=convex_hull(pts)
        print(f"{name}: points={len(pts)} hull_vertices={hull} accepted_candidate_edges={len(edges)} side_tests={tests}")
if __name__=="__main__": main()
