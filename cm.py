from itertools import permutations
a,b = map(int,input().split())
flag = 0
a = list(str(a))
print(a)
a = sorted(a)
print(a)
perm = permutations(a) 
for i in list(perm): 
    string = " "
    for j in i:
        string+=j
    if int(string) > b:
        flag = 1
        break
if flag == 1:
    print(string)
else:
    print(-1)
