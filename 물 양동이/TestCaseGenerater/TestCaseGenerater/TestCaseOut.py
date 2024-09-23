m=[]
def spread(x,y,h):
    global m
    if x<0 or y<0 or x>=W or y>=H or m[y][x]==0 or m[y][x]>h:
        return 0
    temp=m[y][x]
    m[y][x]=0
    spread(x-1,y,temp)
    spread(x,y-1,temp)
    spread(x+1,y,temp)
    spread(x,y+1,temp)

T = 100
for t in range(T):
    o=open("%d.in"%(t+1))
    o2=open("%d.out"%(t+1),"w")
    
    W,H=map(int,o.readline().strip().split())
    
    m=[]
    for i in range(H):
        m.append(list(map(int,o.readline().strip().split())))
    
    x,y=map(int,o.readline().strip().split())
    spread(x-1,y-1,m[y-1][x-1])
    
    for i in range(H):
        o2.write(' '.join(map(str,m[i]))+'\n')
    
    o.close()
    o2.close()