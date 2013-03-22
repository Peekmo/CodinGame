# Read inputs from Standard Input.
# Write outputs to Standard Output.

# CodinGame Maroc
# Exercice Finale
# Par Peekmo


import sys

def fonction(c, nb, out):
    if len(out) == 160: return out
    if c=='0':
        if nb%2 == 1: out+=' '
        else: out+='0'
    else:
        if c=='1': out+='1'
        elif c != ' ':
            mod=4
            if alphabet[(int(c)-2)*6+6] == '-':
                mod=5
            nb=nb%mod
            if nb==0:nb=mod
            out += alphabet[(int(c)-2)*6+nb]
    return out

n = int(raw_input())
alphabet=" abc2,,def3,,ghi4,,jkl5,,mno6,,pqrs7-tuv8,,wxyz9-"
s=raw_input()

c=s[0]
nb=1
out=''
for i in xrange(1,n):
    if len(out) == 160:break
    if s[i] == c: nb += 1
    else:
        out = fonction(c,nb,out)
        nb=1
        c=s[i]
out = fonction(c,nb,out)
print(out)