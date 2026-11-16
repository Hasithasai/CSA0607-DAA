def max_min(a):
 if not a: raise ValueError('empty')
 def f(l,r):
  if l==r:return a[l],a[l],0
  if r==l+1:return (a[l],a[r],1) if a[l]<=a[r] else (a[r],a[l],1)
  m=(l+r)//2; x,y,c=f(l,m);u,v,d=f(m+1,r)
  return min(x,u),max(y,v),c+d+2
 return f(0,len(a)-1)
if __name__=='__main__':
 for a in ([5],[8,2],[9,2,7,1,6],list(range(16))): print(a,'=>',max_min(a))
