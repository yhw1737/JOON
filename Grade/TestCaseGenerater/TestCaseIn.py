import random
T = 1
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    for i in range(101):
        o.write(str(i)+'\n')