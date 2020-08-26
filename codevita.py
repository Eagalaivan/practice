import math 
  
# A function to find largest prime factor 
def maxPrimeFactors (n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
      
    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
# Driver code to test above function 
# n = 15689
# print(maxPrimeFactors(n)) 
  
# n = 28
# print(maxPrimeFactors(n)) 


def lfactor(num): 
    for i in range(num//2,0,-1):  
        if num % i == 0:        
            return i          
l,m=map(int,input().split())
count=0
if(l==m):
    print(0)
elif(l%m==0):
    count=m//2
    print(count)
else:    
    while(l>1):
        l=lfactor(l)
        if(l):
            count+=1
    while(m>1):
        m=lfactor(m)
        if(m):
            count+=1
    print(count)



