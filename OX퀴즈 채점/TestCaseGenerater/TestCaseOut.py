import math
import zipfile
z=zipfile.ZipFile("TestCase.zip","w")
T = 20
for t in range(T):
    o=open("%d.in"%(t+1))
    a,b=map(int,o.readline().strip().split())
    o2=open("%d.out"%(t+1),"w")
    for _ in range(a):
        str=[]
        ans=0
        for i in range(b):
            str.append(o.readline().strip())
        for i in range(b):
            for j in range(b):
                if str[i][j]=='O':
                    ans+=1
                    if i>0:
                        if str[i-1][j]=='O':ans+=1
                    if i<b-1:
                        if str[i+1][j]=='O':ans+=1
                    if j>0:
                        if str[i][j-1]=='O':ans+=1
                    if j<b-1:
                        if str[i][j+1]=='O':ans+=1
        o2.write('%d\n'%ans)
    o.close()
    o2.close()
for t in range(T):
    z.write("%d.in"%(t+1))
    z.write("%d.out"%(t+1))
z.close()