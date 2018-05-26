#Generate uniform random numbers

import random

def zero_one_random():
    return random.randrange(2)

a=input()
b=input()

dif=b-a
p=0
while pow(2,p)<=dif:
    p+=1

ran=dif+1
while ran>dif:
    ran=0
    for i in range(p):
        d=zero_one_random()
        #print d,
        ran=(ran<<1) + d
    #print ran
#print ran
print a+ran
    
