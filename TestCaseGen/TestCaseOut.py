import math
T = 100
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    t=int(o.readline().strip())
    for i in range(t):
        o2.write('*'*(i+1)+'\n')