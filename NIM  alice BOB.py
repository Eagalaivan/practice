def findWinner(array, n): 
    res = 0
    for i in range(n): 
        res ^= array[i] 
       # print(i,res)
    if (res == 0 or n % 2 == 0): 
        return "Alice"
    else: 
        return "Bob"
array = [ 1, 4, 3, 5 ] 
n = len(array) 
print("Winner is ", findWinner(array, n)) 
