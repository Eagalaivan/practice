from collections import deque
def maxSlidingWindow(nums, k):
    q, res = deque(), []
    for i in range(len(nums)):
        if i-k >= 0:
            res.append(nums[q[0]])
            while q and q[0]<=i-k:
                q.popleft()
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)
    res.append(nums[q[0]])
    return sum(res)
N,W,D=map(int,input().split())
nums=list(map(int,input().split()))
k=W
A=maxSlidingWindow(nums,k)
B=maxSlidingWindow(nums,W+D)
z=abs(A-B)
print(A,B,z)
if(A==B):
    print('Both are right')
if(A>B):
    print("Wrong",2)
else:
    print("Right",2)
