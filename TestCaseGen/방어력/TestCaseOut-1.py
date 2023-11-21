import math
T = 20
for t in range(T):
	o=open("%d.in"%(t+1))
	o2=open("%d.out"%(t+1),"w")
	t=int(o.readline().strip())
	for i in range(t):
		l=list(map(float,o.readline().strip().split()))
		i=l[0] * math.floor(l[3] * l[1]) * (100 / (100 + l[2]))
		o2.write("%0.1f"%i+'\n')