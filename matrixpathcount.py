def numberOfPaths(m, n): 
    if(m == 1 or n == 1): 
        return 1
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) 
testcase=int(input())
for i in range(testcase):
    n,m=map(int,input().split())
    print(numberOfPaths(m, n)) 