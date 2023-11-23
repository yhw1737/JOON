import random
T = 20
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    a=(t+1)**2
    b=(t+1)
    o.write('%d %d\n'%(a,b))
    for _ in range(a*b):
        str = ''
        for _ in range(b):
            str+=random.choice(['O','X'])
        str+='\n'
        o.write(str)
    o.close()