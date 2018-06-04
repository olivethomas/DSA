#write a string sinusoidally
"""
Hello World
o/p:  ['e', ' ', 'l', 'H', 'l', 'o', 'W', 'r', 'd', 'l', 'o']
"""

x=raw_input()
i=0
a=[]
b=[]
c=[]
while i<len(x):
    b.append(x[i])
    i=i+1
    if i>=len(x):
        break
    a.append(x[i])
    i=i+1
    if i>=len(x):
        break
    b.append(x[i])
    i=i+1
    if i>=len(x):
        break
    c.append(x[i])
    i=i+1

print a+b+c
