# Read inputs from Standard Input.
# Write outputs to Standard Output.

import sys
from math import fabs

n = int(raw_input())
p=[]
for i in range(0, n):
    p.append(int(raw_input()))

p.sort()

if len(p) >= 2:
    d=fabs(p[0]-p[1])

    for i in range(0, (len(p)-1)):
        if fabs(p[i]-p[i+1]) < d: 
            d=fabs(p[i]-p[i+1])
else:
    d=p[0]
print(int(d))
