# Read inputs from Standard Input.
# Write outputs to Standard Output.

# Par Peekmo
# CodinGame Maroc - Exercice 1
# Langage Python

import sys

n = int(raw_input())
q = int(raw_input())
mime = []
ext = []
for i in range(0, n):
    tab = raw_input().split(' ')
    if mime.count(tab[1]) < 1 or ext.count(tab[0]) < 1:
        ext.append(tab[0])
        mime.append(tab[1])

for i in range(0, q):
    f=raw_input().split('.')
    t=False
    
    for v in range(0, len(ext)):
        if len(f) == 1 or f[len(f)-1] == '':
            break
        elif ext[v].upper() == f[len(f)-1].upper() and mime[v] != 'application/xml':
            print(mime[v])
            t=True
            break
    if t==False:
        print("UNKNOWN")
