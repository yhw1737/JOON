import random
T = 20
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    a=random.randrange(2*13,2**13)
    o.write(str(a)+'\n')
    for _ in range(a):
        a=random.randrange(1,1000)
        s=random.random()*6+0.3
        d=random.randrange(1,1000)
        m=random.random()*50+1
        o.write(str(a)+' '+"%0.1f"%s+' '+str(d)+' '+"%0.1f"%m+'\n')