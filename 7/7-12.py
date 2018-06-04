#implement run-length encoding
"""
3e4f2e
o/p: eeeffffee
aaaabcccaa
o/p: 4a1b3c2a
4a1b3c2a
o/p: aaaabcccaa
stop
"""

def encode(x):
    r=''
    c=1
    for i in range(1,len(x)):
        if x[i-1]!=x[i]:
            r=r+str(c)+x[i-1]
            c=0
        c+=1
    r=r+str(c)+x[i]
    return r

def decode(x):
    r=''
    i=0
    while i<len(x):
        c=0
        while ord(x[i])>=48 and ord(x[i])<=57:
            c=c*10+int(x[i])
            i+=1
        for k in range(c):
            r+=x[i]
        i+=1
    return r

x=raw_input()
while x!='stop':
    if x.isalpha():
        print encode(x)
    elif x.isalnum():
        print decode(x)
    x=raw_input()
