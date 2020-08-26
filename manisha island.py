# testcase =int(input())
# for i in range(1,testcase+1):
#     value = int(input())
#     count=0
#     while (value>=1):
#         value=value//2
#         count+=1
#     print(count)

testcase =int(input())
for i in range(1,testcase+1):
    value = int(input())
    count=1
    while (value>1):
        value=value//2
        count+=1
    print(count)
