from itertools import permutations
a=459
b=500
arr=[]

perm =permutations(str(a))
for i in list(perm):
    arr.append(int(''.join(i)) )
arr.sort()
for i in arr:
    if(i>b):
        print(i)
        break