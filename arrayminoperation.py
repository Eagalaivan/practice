def atobminop(a,b):
    lena=len(a)
    #lenb=len(b)
    calc_boi=1
    diff=0
    min_op=0
    for i in range(lena):
        if(a[i]!=b[i]):
            print(a[i],b[i])
            diff = b[i]-a[i]
            a[i]+=calc_boi
            if(diff == b[i+1]-a[i+1]):
                min_op+=1
            else:
                min_op-=1
    print("i made a[] look like b[]",a)
    print("the min operation required is",min_op)
a = [1, 1, 1, 1, 1, 1]
b = [1, 1, 2, 3, 1, 1]
atobminop(a,b)
# Python3 implementation to find the 
# minimum number of operations in 
# which the array A can be converted 
# to another array B 
  
# Function to find the minimum 
# number of operations in which 
# array A can be converted to array B 
# def checkArray(a, b, n) : 
#     operations = 0
#     i = 0; 
#     while (i < n) : 
#         if (a[i] - b[i] == 0) : 
#             print(a[i],b[i])
#             i += 1
#             continue
#         diff = a[i] - b[i]
#         i += 1
#         while (i < n and a[i] - b[i] == diff) : 
#             i += 1 
#         operations += 1 
#     print(operations)
  
# a = [ 3, 7, 1, 4, 1, 2 ]
# b = [ 3, 7, 3, 6, 3, 2 ]
# size = len(a)
# checkArray(a, b, size)