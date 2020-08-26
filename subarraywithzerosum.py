def subarrayzero(A,N):
    count=0
    for i in range(N):
        sum=0
        for j in range(i,N):
            sum+=A[j]
            if(sum==0):
                count+=1
    print(count)
N=int(input("enter the length of list"))
A=list(map(int,input().split()))
subarrayzero(A,N)