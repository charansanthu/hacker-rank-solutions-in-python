import math
def isprime(n):
    k=int(math.sqrt(n))+1
    for i in range(2,k):
        if n%i==0:
            return False
    return True
n=int(input())
s,c,i=2,0,3
while(s<=n):
    if isprime(i):
        s+=i
        if s<=n and isprime(s):
            c+=1
        i=i+2
    else:
        i=i+2
print(c)
