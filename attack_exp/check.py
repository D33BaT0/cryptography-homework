from Crypto.Util.number import *
from gmpy2 import iroot,powmod,is_prime,gcd,next_prime,invert
n_list = []

e_list = []
c_list = []
index = []
solved = set()
for i in range(21):
    nec = open(f"./Frame{i}",'r').read()

    n = int(nec[:len(nec)//3],16)
    e = int(nec[len(nec)//3:len(nec)//3*2],16)
    c = int(nec[len(nec)//3*2:],16)
    if e==5:
      n_list.append(n)
      e_list.append(e)
      c_list.append(c)
      index.append(i)
print(n_list)
print(c_list)
print(index)
