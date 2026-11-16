# Karatsuba
```text
x=aB+b; y=cB+d
z0=KARATSUBA(b,d); z2=KARATSUBA(a,c)
z1=KARATSUBA(a+b,c+d)-z0-z2
return z2*B^2+z1*B+z0
```
T(n)=3T(n/2)+Θ(n)=Θ(n^log₂3)≈Θ(n^1.585), versus Θ(n²) schoolbook.
