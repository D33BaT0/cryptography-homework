from Crypto.Util.number import *
from gmpy2 import invert
nec1 = open(f"./Frame1",'r').read()

n1 = int(nec1[:len(nec1)//3],16)
e1 = int(nec1[len(nec1)//3:len(nec1)//3*2],16)
c1 = int(nec1[len(nec1)//3*2:],16)

nec = open(f"./Frame18",'r').read()

n = int(nec[:len(nec)//3],16)
e = int(nec[len(nec)//3:len(nec)//3*2],16)
c = int(nec[len(nec)//3*2:],16)

p = GCD(n1,n)
q1 = n1 // p
q = n // p
d1 = invert(e1,(p-1)*(q1-1))
d = invert(e,(p-1)*(q-1))

print("1:",long_to_bytes(pow(c1,d1,n1)).split(b'\x00')[-1])# frame 1
print("18:",long_to_bytes(pow(c,d,n)).split(b'\x00')[-1])# frame 18