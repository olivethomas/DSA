#Compute x/y

a=input()
b=input()
p=32
pow2p=b<<p
q=0
while a>=b:
    while pow2p>a:
        pow2p>>=1
        p=p-1
    q=q+(1<<p)
    a=a-pow2p

print q
    
