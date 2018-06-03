#advancing through an array
"""
3 3 1 0 2 0 1
"""
def canreach(a,n):
    if n==0:
        return True
    j=1
    for i in reversed(range(n)):
        #print a[i],
        if a[i]>=j:
            print
            return canreach(a,i)
        j+=1
    return False

a=map(int,raw_input().split())
print canreach(a,len(a)-1)
    
