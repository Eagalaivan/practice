def circularMatrixFill(array,m_row_end,n_col_end):
    routevalue = 1 
    k_start_row,l_start_col =0,0
    while(k_start_row<m_row_end and l_start_col<n_col_end): 
        
        for i in range(l_start_col,n_col_end): 
            array[k_start_row][i]=routevalue
            routevalue+=1
        k_start_row+=1
    
        for i in range(k_start_row,m_row_end):
          array[i][n_col_end-1]=routevalue
          routevalue+=1
        n_col_end-=1
       
        if(k_start_row<m_row_end):
            
            for i in range(n_col_end-1,l_start_col-1,-1):
                
                array[m_row_end-1][i]=routevalue
                routevalue+=1
            m_row_end-=1
        if(l_start_col<n_col_end):
            for i in range(m_row_end-1,k_start_row-1,-1):
                array[i][l_start_col]=routevalue
                routevalue+=1
            l_start_col+=1

        
    
n=int(input("enter matrix"))
array=[[0 for j in range (n)] for i in range(n)]
circularMatrixFill(array,n,n)
print(array)
# powerpt=0
# result=[]
# for i in range(n):
#     for j in range(n):
#         if(array[i][j]%11==0 or array[i][j]==1):
#             powerpt+=1
#             result.append((i,j))
        
# print("power points",powerpt)  
# # print(result)
# for i in result:
#     print(i)
# print(array)
"""  [1, 2, 3, 4, 5]
    [6, 7, 8, 9, 10]
    [11, 12, 13, 14, 15]
    [16, 17, 18, 19, 20]
    [21, 22, 23, 24, 25] """



