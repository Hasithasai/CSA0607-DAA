def select(a,k):
 if not 1<=k<=len(a):raise ValueError('k out of range')
 if len(a)<=5:return sorted(a)[k-1]
 groups=[a[i:i+5] for i in range(0,len(a),5)];med=[sorted(g)[len(g)//2] for g in groups];p=select(med,(len(med)+1)//2);lo=[x for x in a if x<p];eq=[x for x in a if x==p];hi=[x for x in a if x>p]
 if k<=len(lo):return select(lo,k)
 if k<=len(lo)+len(eq):return p
 return select(hi,k-len(lo)-len(eq))
if __name__=='__main__':
 a=[29,3,17,8,41,12,5,33,21,1,14,27,9,38,6]
 for k in (1,5,8,15):print(k,select(a,k),sorted(a)[k-1])
