#enumerate all primes to n
"""
18
2 3 5 7 11 13 17
"""

n=input()
d={}
d[2]=True
for i in range(3,n+1):
    d[i]=True if i%2==1 else False
for i in range(3,n+1,2):
    for x in range(i**2,n+1,i):
        d[x]=False
ans=[]
for k in d:
    if d[k]:
        ans.append(k)
print ans
