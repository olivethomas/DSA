#the look-and-say problem
"""
8
o/p:  1113213211 //n-th element in look-and-say sequence
"""

def find(a):
    s=''
    i=0
    while i<len(a):
        d=a[i]
        c=1
        while i+1<len(a) and a[i+1]==a[i]:
            c+=1
            i+=1
        s+=str(c)+d
        #print s,
        i+=1
    return s

n=input()
x='1'
for i in range(n-1):
    #print x
    x=find(x)
print x
