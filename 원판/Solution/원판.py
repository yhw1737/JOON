t=int(input())
for _ in range(t):
    n=int(input())
    print(n//80+n%80//40+n%40//20+n%20//10+n%10//5)