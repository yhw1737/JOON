import random
T = 10
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    o.write('100\n')
    for i in range(100):
        k=random.randrange(100, 10000)
        d=random.randrange(1, k)
        o.write('%d %d\n'%(k,d))
    o.close()