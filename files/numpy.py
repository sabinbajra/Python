from array import array

import numpy as np

l = list(range(10))
#print(l)

for i in l: print(i)

vl = [1,2.4,True,"sabin",False,3,3.5]

for i in vl:
    print(type(i))

a = array('f',[2.1,3.4,4,5,6.7])
print(a)

narr = array('i', [2,4,6,8,1,23,5,99,0,12])
print(narr)

zero = array('i',[])
print(zero)