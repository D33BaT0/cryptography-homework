# python2
from Crypto.Util.number import long_to_bytes
import gmpy2
nec = open(f"./Frame6",'r').read()

n = int(nec[:len(nec)//3],16)
e = int(nec[len(nec)//3:len(nec)//3*2],16)
c = int(nec[len(nec)//3*2:],16)


def Pollard_p_1(N):
    a = 2
    while True:
        f = a
        for n in range(1, 200000):
            f = gmpy2.powmod(f, n, N)
            if n % 2 == 0:
                d = gmpy2.gcd(f-1, N)
                if 1 < d < N:
                    return d
        print(a)
        a += 1

p = Pollard_p_1(n)
q = n // p
phi = (p-1) * (q-1)
d = gmpy2.invert(e,phi)
m = long_to_bytes(gmpy2.powmod(c,d,n)).split(b'\x00')[-1]
print(m)

'''
2: b' That is'
6: b' "Logic '
19: b'instein.'
'''