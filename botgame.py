# n, m, x, y = 11,11,3,6
# lx = min(x,n-x+1)
# ly = min(y,m-x+1)
# if min(lx,ly) < 6:
#     print("Mavis wins")
# else:
#     print("Shivam wins")

    
testcase=int(input())
for i in range(testcase):
    n, m, x, y =map(int,input().split())
    lx = min(x,n-x+1)
    ly = min(y,m-x+1)
    if min(lx,ly) < 6:
        print("Mavis wins")
    else:
        print("Shivam wins")
    