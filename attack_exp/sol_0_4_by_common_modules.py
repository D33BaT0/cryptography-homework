from Crypto.Util.number import *
from gmpy2 import gcdext
nec = open(f"./Frame0",'r').read()

n = int(nec[:len(nec)//3],16)
e1 = int(nec[len(nec)//3:len(nec)//3*2],16)
c1 = int(nec[len(nec)//3*2:],16)

nec = open(f"./Frame4",'r').read()

n = int(nec[:len(nec)//3],16)
e2 = int(nec[len(nec)//3:len(nec)//3*2],16)
c2 = int(nec[len(nec)//3*2:],16)
g,a,b = (gcdext(e1,e2))
m = (pow(c1,a,n) * pow(c2,b,n))%n
print(long_to_bytes(m))

'''
0:b'My secre'
4:b'My secre'
'''