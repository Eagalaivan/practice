def isShuffledSubstring(A, B): 
    n = len(A) 
    m = len(B) 
    if (n > m): 
        return False
    else: 
        A = sorted(A) 
        for i in range(m): 
            if (i + n - 1 >= m): 
                return False
            Str = "" 
            for j in range(n): 
                Str += (B[i + j]) 
            Str = sorted(Str) 
            if (Str == A): 
                return True
Str1 = "badbye"
Str2 = "hellobyegoodworld"
a = isShuffledSubstring(Str1, Str2) 
if (a): 
    print("YES") 
else: 
    print("NO") 