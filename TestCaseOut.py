import zipfile
import os

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

z=zipfile.ZipFile("TestCase.zip","w")
for t in range(T):
    z.write("%d.in"%(t+1))
    z.write("%d.out"%(t+1))
z.close()
for t in range(T):
    os.remove("%d.in"%(t+1))
    os.remove("%d.out"%(t+1))