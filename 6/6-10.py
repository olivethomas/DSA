#compute the next permutation
"""
6 2 1 5 4 3 0
o/p: [6, 2, 3, 0, 1, 4, 5]
"""

a=map(int,raw_input().split())
flag=0
for i in reversed(range(len(a))):
    if i==0:
        flag=1
    if a[i-1]<a[i]:
        break
if flag==1:
    print "[]"
else:
    ind=i-1
    j=len(a)-1
    for j in range(len(a)-1,ind,-1):
        if a[j]>a[ind]:
            print a[j]
            break
    a[ind],a[j]=a[j],a[ind]
    #print ind,j
    n=len(a)-ind-1
    j=len(a)-1
    i=ind+1
    while j>ind+(n/2) and i<ind+1+(n/2):
        a[i],a[j]=a[j],a[i]
        j-=1
        i+=1
    print a
        
