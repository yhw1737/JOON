import math
T = 100
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    n=int(o.readline().strip())
    for i in range(n):
        for j in range(n):
            if (i+j)%2==0:
                o2.write('*')
            else:
                o2.write(' ')
        o2.write('\n')