
from itertools import combinations
from itertools import product
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
r1,r2=map(int,input().split())
combo=int(input())
lst=[i for i in range(r1,r2+1)]
print(lst)
perm=product(lst,repeat=combo)
count=0
for i in list(perm):
    print(i,end=' ')
    count+=1
    if(sum(i)%2==0):
        print(i)
        #count+=1
print(count)
def working():
    r1,r2=map(int,input().split())
    combo=int(input())
    lst=[i for i in range(r1,r2+1)]
    print(lst)
    a=len(lst)
    res=(a**combo)//2
    print(res%100000009)

working()