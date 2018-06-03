#multiply 2 arbitrary precision numbers

import math

def add(x,y,i):
    if len(x)==0:
        return y
    else:
        for j in range(0,i):
            y.append(0)
        #print y
        res=[]
        c=0
        i=len(x)-1
        for d2 in reversed(y):
            if i>=0:
                d1=x[i]
                i=i-1
            else:
                d1=0
            res.append((d1+d2+c)%10)
            c=(d1+d2+c)/10
        if c:
            res.append(c)
        return list(reversed(res))

def multiply(x,d):
    c=0
    res=[]
   # print x
    for d1 in reversed(x):
        #print d1*d+c
        res.append((d1*d+c)%10)
        c=(d1*d+c)/10
    if c:
        res.append(c)
    return list(reversed(res))

a=[]
b=[]
x=raw_input()
flag1=1
if x[0]=='-':
    flag1=-1
    x=x[1:]
for d in x:
    a.append(ord(d)-48)
print a

x=raw_input()
flag2=1
if x[0]=='-':
    flag2=-1
    x=x[1:]
for d in x:
    b.append(ord(d)-48)
print b

i=0
pdt=[]
for digit in reversed(b):
    pdt=add(pdt,multiply(a,digit),i)
    #print pdt
    i=i+1
d=flag1*flag2*pdt[0]
pdt.pop(0)
pdt.insert(0,d)
print pdt
