def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def sub(A,B):return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]
def conventional(A,B):
 n=len(A);return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def S(A,B,t=2,c=None):
 if c is None:c={'leaf':0}
 n=len(A)
 if n<=t:c['leaf']+=1;return conventional(A,B)
 h=n//2
 def q(X):return [r[:h] for r in X[:h]],[r[h:] for r in X[:h]],[r[:h] for r in X[h:]],[r[h:] for r in X[h:]]
 a,b,d,e=q(A);f,g,h1,i=q(B)
 m1=S(add(a,e),add(f,i),t,c);m2=S(add(d,e),f,t,c);m3=S(a,sub(g,i),t,c);m4=S(e,sub(h1,f),t,c);m5=S(add(a,b),i,t,c);m6=S(sub(d,a),add(f,g),t,c);m7=S(sub(b,e),add(h1,i),t,c)
 c11=add(sub(add(m1,m4),m5),m7);c12=add(m3,m5);c21=add(m2,m4);c22=add(sub(add(m1,m3),m2),m6)
 return [c11[r]+c12[r] for r in range(h)]+[c21[r]+c22[r] for r in range(h)]
def multiply(A,B):
 n=len(A);N=1
 while N<n:N*=2
 def pad(X):return [r+[0]*(N-n) for r in X]+[[0]*N for _ in range(N-n)]
 c={'leaf':0};z=S(pad(A),pad(B),2,c);return [r[:n] for r in z[:n]],c
if __name__=='__main__':
 for n in (2,4,8):
  A=[[i+j+1 for j in range(n)] for i in range(n)];B=[[int(i==j)+1 for j in range(n)] for i in range(n)];z,c=multiply(A,B);print(n,z==conventional(A,B),c)
