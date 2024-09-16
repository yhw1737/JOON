
T = 10
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    t=int(o.readline().strip())
    ans = 0
    ans2 = 0
    for i in range(t):
        k,d=map(int,o.readline().strip().split())
        if (ans2 > k/d or ans2 == 0):
            ans2 = k/d
            ans = i+1
        o2.write(str(ans))
    o.close()
    o2.close()
