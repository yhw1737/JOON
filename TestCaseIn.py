import random
rl = ['PVT','PV2','PFC','SPC','CPL','SGT','SSG','SFC','MSG','1SG','SGM','CSM']
nl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
T = 10
for t in range(T):
    o=open("%d.in"%(t+1),"w")
    o.write('9\n')
    for i in range(9):
        r=random.choice(rl)
        n=random.choice(nl)
        o.write('%s %s\n'%(r,n))