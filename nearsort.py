n = 5
k = 3
a = [22, 40, 13, 80, 10]
b=[]
c=[]
for i in range(0,k):
    b.append(a[i])
for j in range(k,len(a)):
    c.append(a[j])
b.sort()
c.sort()
a=b+c
print(a)
