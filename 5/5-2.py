#Swap bits
"""
73
1
6
o/p: 11

73
6
0
o/p: 73
"""

x=input()
i=input()
j=input()
if (x>>i)&1 != (x>>j)&1:
    bitmask=(1<<i) | (1<<j)
    x=x^bitmask
print x
