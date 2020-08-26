def array_sum(array,target):
    for i in range(len(array)-1):
        for j in range(1,len(array)):
            if(array[i]+array[j]==target):
                return [i,j]
array=list(map(int,input("array elements").split(" ")))
target=int(input("enter the target sum"))
print(array_sum(array,target))
