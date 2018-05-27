p=list(map(int,raw_input().split()))
a=raw_input().split()
print p
print a

for i in range(len(a)):
    j=i
    while p[j]>=0:
        a[p[j]],a[i]=a[i],a[p[j]]
        t = p[j]
        p[j]=p[j]-len(a)
        j=t
        
print a      
        


