def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 
def rightrotate(arr, n): 
    x = arr[n - 1] 
      
    for i in range(n - 1, 0, -1): 
        arr[i] = arr[i - 1]; 
          
    arr[0] = x; 
  
arr = [1,2,3,4,5]
n=len(arr)
x=3
leftRotate(arr, x, n) 
for i in arr:
    print(i,end=" ")
