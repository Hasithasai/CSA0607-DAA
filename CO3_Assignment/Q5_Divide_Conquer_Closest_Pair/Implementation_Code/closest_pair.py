import math,random
def brute(P):
 best=float('inf');pair=None;c=0
 for i in range(len(P)):
  for j in range(i+1,len(P)):
   c+=1;d=math.dist(P[i],P[j])
   if d<best:best,pair=d,(P[i],P[j])
 return best,pair,c
def closest(P):
 P=sorted(P)
 def f(X):
  if len(X)<=3:return brute(X)
  m=len(X)//2;mid=X[m][0];a=f(X[:m]);b=f(X[m:]);best,pair=(a[0],a[1]) if a[0]<=b[0] else (b[0],b[1]);c=a[2]+b[2];strip=sorted((p for p in X if abs(p[0]-mid)<best),key=lambda p:p[1])
  for i in range(len(strip)):
   j=i+1
   while j<len(strip) and strip[j][1]-strip[i][1]<best:
    c+=1;d=math.dist(strip[i],strip[j])
    if d<best:best,pair=d,(strip[i],strip[j])
    j+=1
  return best,pair,c
 return f(P)
if __name__=='__main__':
 random.seed(7)
 for n in (20,100,300):
  P=[(random.random()*1000,random.random()*1000) for _ in range(n)];a=brute(P);b=closest(P);print(n,abs(a[0]-b[0])<1e-9,a[2],b[2])
