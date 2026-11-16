def subset_sum(a,target):
 m=len(a)//2;L=a[:m];R=a[m:]
 def sums(x):return [(sum(x[i] for i in range(len(x)) if mask>>i&1),mask) for mask in range(1<<len(x))]
 ls=sums(L);rs=sorted(sums(R))
 for s,mask in ls:
  need=target-s;lo=0;hi=len(rs)
  while lo<hi:
   mid=(lo+hi)//2
   if rs[mid][0]<need:lo=mid+1
   else:hi=mid
  if lo<len(rs) and rs[lo][0]==need:
   chosen=[L[i] for i in range(len(L)) if mask>>i&1]+[R[i] for i in range(len(R)) if rs[lo][1]>>i&1]
   return True,chosen,len(ls),len(rs)
 return False,[],len(ls),len(rs)
if __name__=='__main__':print(subset_sum([3,34,4,12,5,2,7,9,11,6],22))
