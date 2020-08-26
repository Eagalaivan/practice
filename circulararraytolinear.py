def convert(k,l,m,n,array):    
    while(k<m and l<n):
        for i in range(l,n):
            print(array[k][i],end=' ')
        k+=1 # left to right
        for i in range(k,m):
            print(array[i][n-1],end=" ")
        n-=1 
        if(k<m):
            for i in range(n-1,l-1,-1):
                print(array[m-1][i],end=" ")
            m-=1
        if(l<n):
            for i in range(m-1,k-1,-1):
                print(array[i][l],end=" ")
        l+=1    
    print()
testcase=int(input())
k,l=0,0
for i in range(testcase):
    m,n=map(int,input("enter row col value").split())
    array = [] 
    a=[]
    for i in range(m):
        a=list(map(int,input().split()))
        array.append(a)
    convert(k,l,m,n,array)
