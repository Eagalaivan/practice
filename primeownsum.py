def isprime(n):
    count=1
    for i in range(2,n//2):
        if(n%i==0):
            count=0
    if(count==0):
        return True
    else:
        return False
a=[]
number=int(input())
numcount=0
sum=0
for i in range(2,number):
    count=1
    for j in range(2,number//2):
        if(i%j==0):
            count=0
    if(count==1):   
        a.append(i)

for j in range(len(a)):
    sum=sum+a[j]
    c=isprime(sum)
    if (c==True):
        numcount+=1
print(numcount)