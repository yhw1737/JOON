import random
T = 10
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    for i in range(100):
        k=random.randrange(100)
        d=random.randrange(100)
        a=random.randrange(100)
        o.write(str(k)+' '+str(d)+' '+str(a)+'\n')