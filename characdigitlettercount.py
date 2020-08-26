Str="a1b2 3./"
alpha=0
spec=0
space=0
num=0
for i in Str:
    if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
        alpha+=1
    elif(ord(i)>=48 and ord(i)<=57):
        num+=1
    elif(i==" "):
        space+=1
    else:
        spec+=1
print("letter(s)",alpha)
print("other",spec)
print("space(s)",space)
print("digit(s)",num)
