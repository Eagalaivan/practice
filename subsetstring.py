def subsetfoundnot(S,string):
    temp=[string[i:j] for i in range(len(string))  for j in range(i + 1, len(string) + 1)]
    #print (temp)
    flag=False
    for i in range(len(temp)):
        for j in S:
            if(temp[i]==j):
                flag=True
            
    if(flag):
        print("subset found")
    else:
        print("no subset found")
S=['a','b','c','d']
string1="ab"
string2="xyz"
subsetfoundnot(S,string2)
subsetfoundnot(S,string1)