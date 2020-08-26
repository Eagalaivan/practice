n=int(input("no of queries..."))
temp=False
elem=int(input("enter the number of elements in set"))
s=[]
stemp=[0]*12
for i in range(n):
    for j in range(elem):
        cin=int(input("items"))
        s.append(cin)
    for j in range(elem):
        if(s[j]==2048):
            stemp[0]+=1
        elif(s[j]==1024):
            stemp[1]+=1
        elif(s[j]==512):
            stemp[2]+=1
        elif(s[j]==256):
            stemp[3]+=1
        elif(s[j]==128):
            stemp[4]+=1
        elif(s[j]==64):
            stemp[5]+=1
        elif(s[j]==32):
            stemp[6]+=1
        elif(s[j]==16):
            stemp[7]+=1
        elif(s[j]==8):
            stemp[8]+=1
        elif(s[j]==4):
            stemp[9]+=1
        elif(s[j]==2):
            stemp[10]+=1
        elif(s[j]==1):
            stemp[11]+=1
    print(stemp,"stemp")
    for j in range(11,1,-1):
        val= stemp[j]/2
        stemp[j-1]+=val
    for j in range(12):
        if(stemp[j]>=pow(2,j)):
            temp=True
            break
    if(temp==True):
        print("YES")
    else:
        print('NO')
print(s)
print(stemp)