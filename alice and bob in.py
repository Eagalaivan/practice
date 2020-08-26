x=int(input())
for i in range(x):
    n=int(input())
    l=list(map(int,input().split()))
    k=0
    for i in range(0,n):
        while(l[i]-i-1>=0):
            l[i]=l[i]-i-1
            k+=1
    if(k%2==0):
        print("BOB")
    else:
        print("ALICE")


# testcase=int(input('test'))
# for i in range(testcase):
#     len_list=int(input())
#     list=list(map(int,input().split()))
#     value=0
#     for i in range(0,len_list):
#         while(list[i]>=1):
#             list[i]=list[i]-1
#             value+=1
#     if(value%2==0):
#         print("BOB")
#     else:
#         print("ALICE")

