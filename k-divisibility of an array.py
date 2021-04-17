n,k=map(int,input().split())
c=0
l=list(map(int,input().strip().split(' ')))
h=[0]*k
for i in l:
    h[i%k]+=1
c+=h[0]*(h[0]-1)//2
i=1
while i<=(k//2) and i!=(k-i):
    c+=h[i]*h[k-i]
    i+=1
if(k%2==0):
    c+=h[k//2]*(h[k//2]-1)//2
print(c)
