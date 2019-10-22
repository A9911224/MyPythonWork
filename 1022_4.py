# coding: utf-8
a = input("")
b = input("")
c = input("")
d = input("")

aa = a.split(" ")
bb = b.split(" ")
cc = c.split(" ")
dd = d.split(" ")

good=0
normal=0
bad=0

def charm(x):
    return int(x[0])+int(x[1])+int(x[2])+int(x[3])+int(x[4])

good=0
normal=0
bad=0

S=[aa,bb,cc,dd]
for q in S:
    if charm(q)>=25:
        good=good+1
    elif charm(q)>=21:
        normal=normal+1
    else:
        bad=bad+1
    

print("CP",good)
print("chance",normal)
print("without chance",bad)
