def mul(m,n):
    if m == 1:
        return 1
    elif m ==0 or n == 0:
        return 0
    return m + mul(m, n-1)
print(mul(50,100))