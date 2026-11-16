def merge_sort(a):
 if len(a)<2:return a[:]
 m=len(a)//2; x=merge_sort(a[:m]);y=merge_sort(a[m:]);o=[]
 while x and y:o.append(x.pop(0) if x[0]<=y[0] else y.pop(0))
 return o+x+y
def quick_sort(a):
 stats={'partitions':[],'max_depth':0}
 def f(x,d):
  stats['max_depth']=max(stats['max_depth'],d)
  if len(x)<2:return x
  p=x[-1];l=[v for v in x[:-1] if v<=p];r=[v for v in x[:-1] if v>p];stats['partitions'].append((len(l),len(r)))
  return f(l,d+1)+[p]+f(r,d+1)
 return f(a[:],1),stats
if __name__=='__main__':
 for a in ([4,2,6,1,3,5,7],list(range(1,8)),list(range(7,0,-1)),[3,1,3,2,3,0]):print(a,merge_sort(a),quick_sort(a))
