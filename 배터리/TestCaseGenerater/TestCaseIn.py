import random
T = 1
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    o.write("100\n")
    for i in range(100):
        n=random.randint(1,50)
        m=random.randint(1,100)
        o.write("%d %d\n"%(n,m))
    o.close()