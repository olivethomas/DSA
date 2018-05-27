#Buy and sell stock twice
"""
12 11 13 9 12 8 14 13 15
o/p: 10
"""

a=map(int,raw_input().split())
minsofar=32767
maxprofit=-32768
mp=[]
for x in a:
    minsofar=min(minsofar,x)
    maxprofit=max(maxprofit,x-minsofar)
    mp.append(maxprofit)
maxsofar=-32768
maxprofit=0
for i in range(len(a)-1,2,-1):
    maxsofar=max(maxsofar,a[i])
    maxprofit=max(maxprofit,maxsofar-a[i]+mp[i-1])
print max(maxprofit,mp[len(mp)-1])
