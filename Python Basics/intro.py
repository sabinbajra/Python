# This is the comment in python
"""
This is multiple line
comment in
Python


a = 0
b = 1
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

"""

import numpy as np

# np.empty([10, 10])
# print(np.empty([5, 5], dtype=float))
# print(np.zeros(10, dtype=int))
# print(np.zeros(10, dtype=int))
#print(np.ones((3, 5), dtype=int))
#print(np.full((4,4), "a"))
#print(np.full((3,5), 1.2))
a = np.arange(1,100)
#print(a)

for i in a:
    i = i + 2
    print(i)

