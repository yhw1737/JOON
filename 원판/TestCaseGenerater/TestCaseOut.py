import math
import zipfile

T = 100
for t in range(T):
    o=open("%d.in"%(t+1))
    a=int(o.readline().strip())
    o2=open("%d.out"%(t+1),"w")
    for _ in range(a):
        n=int(o.readline().strip())
        o2.write("%d\n"%(n//80+n%80//40+n%40//20+n%20//10+n%10//5))
    o.close()
    o2.close()

z=zipfile.ZipFile("TestCase.zip","w")
for t in range(T):
    z.write("%d.in"%(t+1))
    z.write("%d.out"%(t+1))
z.close()