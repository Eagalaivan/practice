n = int(input())
arr = []
sum = 0
count = 0
if n > 1:
    for i in range(2, n + 2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)
def isprime(sum):
    for i in range(2, (sum // 2) +2):
        if sum % i == 0:
            return False
        else:
            return True
for i in range(0, len(arr)):
    sum = sum + arr[i]
    if sum <= n:
        if isprime(sum):
            count = count + 1
print(count)