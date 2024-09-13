
T=1
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    g=int(o.readline().strip())
    for i in range(g):
        n,m=map(int,o.readline().strip().split())
        ans = int((90-m)/n)+((90-m)%n!=0)
        if ans < 0: ans = 0
        o2.write("%d\n"%ans)
    o.close()
    o2.close()