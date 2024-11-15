x,y,z = map(int,input().split())
t_m = z * 24 * 60
r_m = x*y
#res = t_m - r_m
if(r_m <= t_m):
    print("YES")
else:
    print("NO")
