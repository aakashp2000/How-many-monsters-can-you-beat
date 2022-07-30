n = int(input()) #2
lev = int(input()) #123
p = []
b = []
a = []
ans = 0
for i in range(n):
   p.append(int(input())) #[78,130]
for j in range(n):
   b.append(int(input())) #[10,0]
for k in range(n):
   a.append([p[k], b[k]]) #[[78,10],[130,0]]
a.sort()
for z in a:
   if z[0] > lev:
       break
   lev += z[1]
   ans += 1
print(ans)
