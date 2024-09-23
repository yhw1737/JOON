import random
T = 100
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    W = random.randrange(3,50)
    H = random.randrange(3,50)
    o.write('%d %d\n'%(W,H))
    for i in range(H):
        for j in range(W):
            k=random.randrange(1,10)
            o.write('%d'%k)
            if j!=W-1:
                o.write(' ')
        o.write('\n')
    x = random.randrange(1,W)
    y = random.randrange(1,H)
    o.write('%d %d\n'%(x,y))
    o.close()