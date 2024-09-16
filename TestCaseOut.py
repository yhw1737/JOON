import zipfile
import os

def my_round(num:float)->int:
    if num < 0:
        return -my_round(-num)
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
T = 10
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    t=int(o.readline().strip())
    for i in range(t):
        k,d=map(int,o.readline().strip().split())
        o2.write('%.1f:1\n'%(my_round(d/k*10)/10))
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