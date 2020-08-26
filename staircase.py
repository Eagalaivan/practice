def fibo(n):
    if(n<=1):
        return n
    return (fib(n-1)+fib(n-2))
def count(num):
    return  (fib(num+1))
num=int(input())
print(count(num))