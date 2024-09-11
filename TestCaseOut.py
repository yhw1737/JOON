import zipfile
import os

a = [[]]
def determine(str):
    if str=='PVT':
        return 0
    if str=='PV2':
        return 1
    if str=='PFC':
        return 2
    if str=='SPC':
        return 3
    if str=='CPL':
        return 3
    if str=='SGT':
        return 4
    if str=="SSG":
        return 5
    if str=="SFC":
        return 6
    if str=='MSG':
        return 7
    if str=='1SG':
        return 7
    if str=='SGM':
        return 8
    if str=='CSM':
        return 8
T = 10
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    n=int(o.readline().strip())
    for k in range(n):
        txt=o.readline().strip()
        a[determine(txt[0])]+=' '+txt[1]
    for k in range(9):
        if a[k]!=[]:
            o2.write("E%d %s",(k+1,a[k]))
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