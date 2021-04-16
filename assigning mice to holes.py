n=int(input())
m=[int(i) for i in input().split()]
h=[int(i) for i in input().split()]
m=sorted(m)
h=sorted(h)
l=[]
for i in range(len(m)):
    l.append(abs(m[i]-h[i]))
print(max(l))
