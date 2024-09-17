import random
T = 10
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    g=random.randrange(1,100)
    o.write('%d\n'%g)
    for i in range(g):
        k=random.randrange(1, 100)
        o.write('%d\n'%k)
    o.close()