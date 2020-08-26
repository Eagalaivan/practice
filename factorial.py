def fact(n):
    if(n>0):
        return fact(n*(n-1))
    else:
        return n
n=5
fact(n)
