def nearkfactor(N,k):
    if(N%k!=0):
        print(1)
    else:
        arr=[]
        for i in range(1,N+1):
            if(N%i==0):
                arr.append(i)
        # for i in arr:
        #     if(arr[i]>k):
        #         print(arr[i])
        #         break
        print(arr[-k])
N,k=map(int,input().split(','))
nearkfactor(N,k)
