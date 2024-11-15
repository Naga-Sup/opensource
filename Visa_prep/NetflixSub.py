a,b,c,z = map(int,input().split())
a1 = max(a,b)
a2 = max(b,c)
if a1==a2:
    a2 = max(a,b)
if a1+a2>=z:
    print("YES")
else:
    print("NO")
