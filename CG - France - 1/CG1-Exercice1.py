# Read inputs from Standard Input.
# Write outputs to Standard Output.

# Par Peekmo
# CodinGame 1 - Exercice 1
# Langage Python

import sys

L = int(raw_input())
H = int(raw_input())
T = raw_input().upper()
i=0
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
alphabet = list()
while i < H:
    x = raw_input()
    alphabet.append(x)
    i += 1

v=0
while v<H:
    for c in T:
        # Cherche la pos du nbre dans l'alphabet
    	pos = lettres.find(c)
        if (pos == -1): pos = len(lettres)-1
        sys.stdout.write((alphabet[v])[pos*L:(pos*L)+L])
    v+=1
    print('')