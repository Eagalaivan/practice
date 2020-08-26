def cal_len(n):
    lenght=0
    while(n!=0):
        lenght+=1
        n//=10
    return lenght
num=int(input())
remainder=0
Sum=0
length=cal_len(num)
temp=num
while(temp>0):
    remainder=temp%10
    Sum=Sum+(remainder**length)
    length-=1
    temp=temp//10
if(Sum==num):
    print("disarium")
else:
    print("not disarium")