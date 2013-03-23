# Read inputs from Standard Input.
# Write outputs to Standard Output.

# CodinGame France 2
# Exercice 1
# Par Peekmo

import sys

def tobi(l):
    b=''
    l=ord(l)
    v=64
    while 1:
        if l/v > 0: 
            b+='1'
            l-=v
        else: b+='0'
        if v==1: break
        v/=2
    return b

def trans(b):
    r=''
    l=None
    for c in b:
        if c==l: r+='0'
        else:
            if l != None: r+=' '
            l=c
            if l=='1': r+='0 0'
            else: r+='00 0'
    return r

n = raw_input()
b=''

for l in n:
    b+=tobi(l)
    
print trans(b)