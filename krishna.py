# T =  int(input())
# arr = []
# arr1 = []
# for i in range(0, T):
#     N = int(input())
#     for i in range(1):
#         arr=list(map(int,input().split()))
#     arr.sort()
#     count = arr[0]
#     print(count)
#     for i in range(1, len(arr)):
#         count = count + arr[i]
#         arr1.append(count)
# print(sum(arr1))


T =  1
arr = []
arr1 = []
for i in range(0, T):
    N = 4
    for i in range(1):
        arr=[1,2,3,4]
    arr.sort()
    count = arr[0]
    print(count)
    for i in range(1, len(arr)):
        count = count + arr[i]
        arr1.append(count)
print(sum(arr1))
