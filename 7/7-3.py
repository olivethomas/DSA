#compute the spreadsheet column encoding
"""
ZZ
o/p: 702
"""

s=raw_input()
v=0
for l in s:
    v=v*26+(ord(l)-64)
print v
