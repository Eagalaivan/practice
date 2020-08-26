n = int(input("Enter a number: "))
flag = 0
for i in range(n):
    if i * (i + 1) == n:
        flag = 1
        break
if flag==1:
    print("Pronic number")
else:
    print("not pronic")
