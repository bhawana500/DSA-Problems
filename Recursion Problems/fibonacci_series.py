#In this, Fibonacci series starts from 0 means basically, 0 1 1 3 5 8...and so on 
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Enter the nth term: "))
k=fibonacci(n)
print(k)