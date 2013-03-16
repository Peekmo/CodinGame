# Read inputs from Standard Input.
# Write outputs to Standard Output.

# Par Peekmo
# CodinGame 1 - Exercice 2
# Langage Python

import sys

n = int(raw_input())
val = raw_input().split(' ')
vmax = vmin = int(val[0])
p=pmax=0
for i in range(1, n):
    v = int(val[i])
    if v > vmax:
        if p<pmax: pmax=p
        vmax = vmin = v
    else:
        if v<vmin: vmin = v
        p=vmin - vmax
if p<pmax: pmax=p
print (pmax)
