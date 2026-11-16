def binary_search(a,t):
 l,r=0,len(a)-1;c=0
 while l<=r:
  m=(l+r)//2;c+=1
  if a[m]==t:return m,c
  if a[m]<t:l=m+1
  else:r=m-1
 return -1,c
if __name__=='__main__':
 a=list(range(0,64,2))
 for t in (0,30,62,31,-2,100):print(t,binary_search(a,t))
