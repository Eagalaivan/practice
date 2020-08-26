# def search(pat, txt): 
#     count=0
#     M = len(pat) 
#     N = len(txt)
#     for i in range(N - M + 1): 
#         j = 0
#         while(j < M): 
#             if (txt[i + j] != pat[j]): 
#                 break
#             j += 1
#         if (j == M):  
#             count+=1
#     print("Pattern found "+str(count)+" times") 
# txt = "weliveinsociety"
# pat = "live"
# search(pat, txt) 

d = 256
  

def searchrobin(pat, txt, q): 
    M = len(pat) 
    N = len(txt) 
    i = 0
    j = 0
    p = 0    
    h = 1
    t=0   
    for i in range(M-1): 
        h = (h * d)% q  
    for i in range(M): 
        p = (d * p + ord(pat[i]))% q 
        t = (d * t + ord(txt[i]))% q  
    for i in range(N-M + 1):      
        if p == t:           
            for j in range(M): 
                if txt[i + j] != pat[j]: 
                    break
            j+= 1           
            if j == M: 
                print ("Pattern found at index " + str(i))         
        if i < N-M: 
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q            
            if t < 0: 
                t = t + q 
txt = "we live in a society"
pat = "society"
q = 101 
searchrobin(pat, txt, q)
