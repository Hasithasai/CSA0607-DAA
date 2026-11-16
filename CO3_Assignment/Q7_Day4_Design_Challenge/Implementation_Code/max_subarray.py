def dc(a):
 if not a:raise ValueError('empty')
 def f(l,r):
  if l==r:return a[l],l,r
  m=(l+r)//2;x=f(l,m);y=f(m+1,r);s=0;bl=float('-inf');i=m
  for k in range(m,l-1,-1):
   s+=a[k]
   if s>bl:bl=s;i=k
  s=0;br=float('-inf');j=m+1
  for k in range(m+1,r+1):
   s+=a[k]
   if s>br:br=s;j=k
  return max((x,y,(bl+br,i,j)),key=lambda z:z[0])
 return f(0,len(a)-1)
def brute(a):
 best=float('-inf');ans=None
 for i in range(len(a)):
  s=0
  for j in range(i,len(a)):
   s+=a[j]
   if s>best:best,ans=s,(best,i,j)
 return best,ans[1],ans[2]
if __name__=='__main__':
 for a in ([-2,1,-3,4,-1,2,1,-5,4],[-5,-2,-8],[1,2,3,-2,5]):print(a,dc(a),brute(a),dc(a)[0]==brute(a)[0])
