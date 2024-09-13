import zipfile
import os

T=1
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    g=int(o.readline().strip())
    for i in range(g):
        n,m,k=map(int,o.readline().strip().split())
        o2.write("%d\n"%(n*m*k))
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