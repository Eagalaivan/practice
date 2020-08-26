def maxChainLength(arr,n):
    max = 0
    mcl = [1 for i in range(n)] 
    for i in range(1, n): 
        for j in range(0, i): 
            if (arr[i][0] > arr[j][1] and mcl[i] < mcl[j] + 1): 
                mcl[i] = mcl[j] + 1
    for i in range(n): 
        if (max < mcl[i]): 
            max = mcl[i] 
    print(max)
testcase=int(input("test case"))
for i in range(testcase):
    N=int(input("no of pairs"))
    str=list(map(int,input().split()))
    a=[]
    for i in range(0,len(str),2):
        a.append((str[i],str[i+1]))
    #print(a)
    n=len(a)
    maxChainLength(a,n)
