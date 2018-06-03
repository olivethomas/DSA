#convert from roman to decimal
"""
LVIIII
o/p:  59
"""

while 1:
    a=raw_input()
    print a

    val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ans=0
    pval=0
    for x in reversed(a):
        v=val[x]
       # print v,pval,
        if v<pval:
            ans=ans-v
        else:
            ans=ans+v
       # print ans
        pval=v

    print ans
