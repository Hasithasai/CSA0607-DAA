def karatsuba(x,y,c=None):
 if c is None:c={'leaf_products':0}
 if x<10 or y<10:c['leaf_products']+=1;return x*y
 m=max(len(str(x)),len(str(y)))//2;p=10**m;a,b=divmod(x,p);d,e=divmod(y,p)
 z0=karatsuba(b,e,c);z2=karatsuba(a,d,c);z1=karatsuba(a+b,d+e,c)-z0-z2
 return z2*p*p+z1*p+z0
if __name__=='__main__':
 for n in (2,4,8,16,32):
  x=int('9'*n);y=int('8'*n);c={'leaf_products':0};print(n,karatsuba(x,y,c)==x*y,c)
