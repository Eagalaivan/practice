x=int(input("Enter a number for x: "))
y=int(input("Enter a number for y: "))
def findProduct(x,y):
    if y<0:
        return -findProduct(x,-y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
         return x+ findProduct(x,y-1)
print("product of two numbers: ",findProduct(x,y))
