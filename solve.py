# def wordBreak(wordList, word): 
#     if word == '': 
#         return True
#     else: 
#         wordLen = len(word) 
#         return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]) 
# wordList= [ 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
# word ="ilikeicecreamandmango"
# # 
# # print(wordBreak(wordList,word))

# # for i in range(0,len(word)+1):
# #     print(word[:i])

# for i in range(len(wordList)):
#     res =word.split()
# print(res)
s = "ilikeicecreamandmango"
dictionary =  {  'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'}
result = []
max_l = len(max(dictionary, key=len))
length = len(s) + 1
for j in range(1,length):
    i = j - 1
    flag = 0
    ans = []
    x = 0

    if j > max_l:
        x = j - max_l
    while(i >= x):
        if s[i:j] in dictionary:
            if i > 0 and result[(i - 1)]:
                    temp = list((map(lambda x : x + " "+ s[i:j],\
                    result[(i - 1)])))
                    for elem in temp:
                        ans.append(elem)
                    flag = 2
            else:
                flag = 1
                result.append([s[i:j]])
        i=i-1
    if flag == 0:
        result.append([])
    if flag == 2:
        result.append(ans)
if s in dictionary:
  result[len(s) - 1].append(s)

temp = ", result [{}]: "
    
print(result[len(s) - 1])
