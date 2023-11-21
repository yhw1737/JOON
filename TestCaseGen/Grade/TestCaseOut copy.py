def get_grade(score):
	return "FFFFFFDCBAA"[score//10]
T=1
for t in range(T):
    o2=open("%d.out"%(t+1),"w")
    for i in range(101):
        o2.write(get_grade(i)+'\n')