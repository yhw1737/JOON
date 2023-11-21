import math
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
        k,d,a=map(int,o.readline().strip().split())
        if d==0:
            o2.write('Perfect\n')
            continue
        o2.write('%.1f\n'%(my_round((k+a)/d*10)/10))
