def decimal(a):
    res=0
    for i,j in enumerate(a):
        if j=='1':
            res+=2**(len(a)-i-1)
    return res
a,b=input(),input()
n=decimal(a)
m=decimal(b)
print(n+m)