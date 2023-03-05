from Crypto.Util.number import *
from gmpy2 import iroot
nec = open(f"./Frame14",'r').read()

n = int(nec[:len(nec)//3],16)
e = int(nec[len(nec)//3:len(nec)//3*2],16)
c = int(nec[len(nec)//3*2:],16)

# (a+b)(a-b) = a^2-b^2=>a^2-n=b^2
a = iroot(n,2)[0]+1
for i in range(a,a+100000000):
    if iroot(i**2 - n,2)[1]:
        b = iroot(i**2 - n,2)[0]
        p = (i+b)
        q = (i-b)
        print(p)
        print(q)
        break

d = inverse(e,(p-1)*(q-1))
print(long_to_bytes(pow(c,d,n)).split(b'\x00')[-1])