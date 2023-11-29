import math
import zipfile
import os

def decimal(a):
    res=0
    for i,j in enumerate(a):
        if j=='1':
            res+=2**(len(a)-i-1)
    return res

T = 300
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    n=decimal(o.readline().strip())
    m=decimal(o.readline().strip())
    o2.write(str(n+m))
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