import random
T = 100
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    a=random.randrange(400,500)
    o.write("%d\n"%a)
    for _ in range(a):
        o.write('%d\n'%random.randint(0,1000000))
    o.close()