from itertools import product
# from itertools import permutations
# def evend(roll):
#     for dat in roll:

# ranges = list(map(int,input().strip().split()))
# ranges=[4,5]
# k = 3
# permuted = []
# for roll in product(ranges, repeat = k):
#     permuted.append(roll)
# print(permuted)
# count=0
# for i in permuted:
#     if(sum(i)%2==0):
#         count+=1
# print(count)
def evenodd(low,high,K):
    ranges=[]
    count=0
    for i in range(low,high+1):
        ranges.append(i)
    # print(ranges)
    for roll in product(ranges, repeat = K):
        if(sum(roll)%2==0):
            count+=1
    return count
low,high=map(int,input().strip().split())
K=int(input())
print(evenodd(low,high,K))


# countt=0
# for roll in permutations([1,2,3,4,5,6,7,8,9,10],2):
#     print(roll)
#     if(sum(roll)%2==0):
#         countt+=1
# print(countt)