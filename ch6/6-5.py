#Delete duplicates from a sorted array

a=map(int,raw_input().split())
n=len(a)
f=0
l=None
for x in a:
    if l==None or l!=x:
        a[f]=x
        f+=1
        l=x

a=a[:f]
print a
