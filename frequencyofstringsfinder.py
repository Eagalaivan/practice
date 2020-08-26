def frequency_finder(test_str,s):
    all_freq={}
    for i in test_str: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    no_of_replaces=0
    for keys in all_freq:
        if(all_freq[keys]==2 or all_freq[keys]==1):
            continue
        no_of_replaces+=all_freq[keys]//2
    print(all_freq)
    print(no_of_replaces)
    s.append(no_of_replaces)
n=int(input())
s=[]
for i in range(n):
    test_str=input()
    frequency_finder(test_str,s)
c=sum(s)
res=(c)
print(res)