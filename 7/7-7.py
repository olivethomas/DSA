#compute all mnemonics for a phone number
"""
2276696
o/p: all character sequences corresp. to the number
"""

def findcomb(a,d,s):
    if len(a)==0:
        #print "0"
        return [s]
    #print a
    x=a[0]
    res=[]
    for letter in d[x]:
        c=findcomb(a[1:],d,s+letter)
        res=res+c
    return res

a=map(int,list(raw_input()))
if len(a)!=7 and len(a)!=10:
    print len(a)
    exit()
d=["0","1","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
b=findcomb(a,d,"")
print b
