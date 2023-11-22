import math
T = 45
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    t=int(o.readline().strip())
    dp=[0,1]
    for i in range(t+1):
        if i>1:
            dp.append(dp[i-2]+dp[i-1]+1)
    o2.write(str(dp[t]))