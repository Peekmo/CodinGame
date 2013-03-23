# Read inputs from Standard Input.
# Write outputs to Standard Output.

# CodinGame France 1
# Exercice 3
# Par Peekmo

import sys

n = int(raw_input())

mini=None
last=None
tab=[]

for i in xrange(0,n):
    x,y=raw_input().split(' ')
    x,y=int(x),int(y)
    tab.append(y)
    if mini==None or x<mini: mini=x
    if last==None or x>last: last=x
tab.sort()
t=tab[len(tab)/2]
d=last-mini
for i in xrange(len(tab)):
    d+=abs(tab[i]-t)
print(d)
