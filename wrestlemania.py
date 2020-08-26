t=int(input("testcase no.. "))
for i in range(t):
    a=input("number.. ")
    num=int(a)
    if(num%21==0):
        print("The streak is broken")
        continue
    if("21" in a):
        print("The streak is broken")
    else:
        print("The streak lives still in our heart!")

