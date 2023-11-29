import random
T = 300
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    a=random.randrange(30)
    b="1"
    c="1"
    for _ in range(a):
        b+=random.choice(['0','1'])
        c+=random.choice(['0','1'])
    o.write(b.lstrip('0')+'\n'+c.lstrip('0'))
    o.close()