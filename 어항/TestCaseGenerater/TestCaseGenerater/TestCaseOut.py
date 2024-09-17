
T = 10
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    t=int(o.readline().strip())
    ans = 0
    for i in range(t):
        k=int(o.readline().strip())
        ans+=k*(i+1)
    o2.write(str(ans))
    o.close()
    o2.close()
