#compute all valid ip addresses
"""
19216811
o/p:        1.92.168.11
            19.2.168.11
            19.21.68.11
            19.216.8.11
            19.216.81.1
            192.1.68.11
            192.16.8.11
            192.16.81.1
            192.168.1.1
"""

def isvalid(s):
    if len(s)<1 or len(s)>3:
        return False
    if s[0]=='0' and len(s)>1:
        return False
    v=int(s)
    return v>=0 and v<256

ip=raw_input()

for i in range(1,4):
    if i>=len(ip):
        break
    first=ip[:i]
    if isvalid(first):
        for j in range(1,4):
            if i+j>=len(ip):
                break
            second=ip[i:i+j]
            if isvalid(second):
                for k in range(1,4):
                    if i+j+k>=len(ip):
                        break
                    third=ip[i+j:i+j+k]
                    if isvalid(third):
                        fourth=ip[i+j+k:]
                        if isvalid(fourth):
                            print first+'.'+second+'.'+third+'.'+fourth
                
