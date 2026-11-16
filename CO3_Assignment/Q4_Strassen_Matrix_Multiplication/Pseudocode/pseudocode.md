# Strassen
Seven block products: M1=(A11+A22)(B11+B22); M2=(A21+A22)B11; M3=A11(B12−B22); M4=A22(B21−B11); M5=(A11+A12)B22; M6=(A21−A11)(B11+B12); M7=(A12−A22)(B21+B22).
C11=M1+M4−M5+M7; C12=M3+M5; C21=M2+M4; C22=M1−M2+M3+M6. Pad to next power of two and crop. T(n)=7T(n/2)+Θ(n²)=Θ(n^2.807).
