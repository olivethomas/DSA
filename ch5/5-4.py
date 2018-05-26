#find closest integer with same weight
""" 7
output: 11
"""

n=input()
lsb=n&1
a=n
i=0
a=a>>1
while a!=0:
    if lsb!=a&1:
        break
    i+=1
    a=a>>1
n=n^(3<<i)
print n
