# Read inputs from Standard Input.
# Write outputs to Standard Output.

# CodinGame Maroc
# Exercice 3
# Par Peekmo

import sys

class train:
    def __init__(self):
        self.g=0
        self.p=0

L,C,N=raw_input().split(' ')
L,C,N=int(L),int(C),int(N)
tab=[]

for i in range(N): tab.append(int(raw_input()))

t=[]
for i in range(N):
    g=tab[i]
    w=i
    for y in range(N-1):
        w+=1
        if w>=N: w=w-N 
        if g+tab[w] > L: break
        else: g+=tab[w]

    places = train()
    places.g=g
    places.p=w
    t.append(places)

p=0
s=0
for i in xrange(C):
   s+=t[p].g
   p=t[p].p
print(s)
