# # class subsetsum:
# #     def subsum(self,array, sum: int ) -> int:
# #         sumdict = {0:1}
# #         n=len(array)
# #         count = 0
# #         s =0
# #         for i in array:
# #             s = s+i
# #             print(s)
# #             print("s-sum",s-sum)
# #             if s-sum in sumdict:
# #                 count+=sumdict[s-sum]
# #                 print(count)
# #             if s in sumdict:
# #                 sumdict[s]+=1
# #             else:
# #                 sumdict[s]=1
# #         print(sumdict)
# #         return count
# # array= [15, 22, 14, 26, 32, 9, 16, 8]
# # sum=4
# # obj = subsetsum()
# # print(obj.subsum(array,sum))


# # def subArraySum(arr, n, sum): 

# #     for i in range(n): 
# #         curr_sum = arr[i] 
      
  
# #         j = i + 1
# #         while j <= n: 
# #             print(curr_sum)
# #             if curr_sum == sum: 
# #                 print ("Sum found between") 
# #                 print("indexes % d and % d"%( i, j-1)) 
                  
# #                 return 1
                  
# #             if curr_sum > sum or j == n: 
# #                 break
              
# #             curr_sum = curr_sum + arr[j] 
# #             j += 1
  
# #     print ("No subarray found") 
# #     return 0

# # arr= [15, 22, 14, 26, 32, 9, 16, 8]
# # n=len(arr)
# # sum=53
# # subArraySum(arr,n,sum)

# # A recursive solution for subset sum 
# # problem 
  
# # Returns true if there is a subset  
# # of set[] with sun equal to given sum 
# def isSubsetSum(set, n, sum) : 
    
#     # Base Cases 
#     if (sum == 0) : 
#         print(set)
#         return True
        
#     if (n == 0 and sum != 0) : 
#         return False
   
#     # If last element is greater than 
#     # sum, then ignore it 
#     if (set[n - 1] > sum) : 
#         return isSubsetSum(set, n - 1, sum)
   
#     # else, check if sum can be obtained 
#     # by any of the following 
#     # (a) including the last element 
#     # (b) excluding the last element    
#     return isSubsetSum( 
# set, n-1, sum) or isSubsetSum( 
# set, n-1, sum-set[n-1]) 
      
      
# # Driver program to test above function 
# set = [15, 22, 14, 26, 32, 9, 16, 8]
# sum = 53
# n = len(set) 
# if (isSubsetSum(set, n, sum) == True) : 
#     print("Found a subset with given sum",isSubsetSum(set, n, sum)) 
# else : 
#     print("No subset with given sum") 



# Python program to print all subsets with given sum 

# def printAllSubsetsRec(arr, n, v, sum) : 
#     if (sum == 0) : 
#         for value in v : 
#             print(value, end=" ") 
#         print() 
#         return
#     if (n == 0): 
#         return 
#     printAllSubsetsRec(arr, n - 1, v, sum) 
#     v1 = [] + v 
#     v1.append(arr[n - 1]) 
#     printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1]) 
# def printAllSubsets(arr, n, sum): 
#     v = [] 
#     printAllSubsetsRec(arr, n, v, sum) 
# arr = [15, 22, 14, 26, 32, 9, 16, 8]; 
# sum = 53
# n = len(arr) 
# printAllSubsets(arr, n, sum) 
def printsubsets(arr, n, v, sum) : 
    if (sum == 0) : 
        for value in v : 
            print(value, end=" ") 
        print() 
        return
    if (n == 0): 
        return 
    printsubsets(arr, n - 1, v, sum) 
    v1 = [] + v 
    v1.append(arr[n - 1]) 
    printsubsets(arr, n - 1, v1, sum - arr[n - 1]) 
def printAllSubsets(arr, n, sum): 
    v = [] 
    printsubsets(arr, n, v, sum) 
arr = [15, 22, 14, 26, 32, 9, 16, 8]; 
sum = 53
n = len(arr) 
printAllSubsets(arr, n, sum) 

