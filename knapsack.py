def knapSack(W, wt, val, n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                   knapSack(W, wt, val, n-1))  
val = [] 
wt = [] 
W = 50
items = [

  {'val': 150, 'wt': 20},

  {'val': 100, 'wt': 20},

  {'val': 120, 'wt': 30}

]
for i in range(3):
    val.append(items[i]['val'])
    wt.append(items[i]['wt'])
print(val,wt)
n=len(val)
print (knapSack(W, wt, val, n))