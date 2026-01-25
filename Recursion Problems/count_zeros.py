def count_zeros(n):
    if n == 0:
        return 1
    elif n < 10 and n !=0:
        return 0
    elif n%10 == 0:
        return 1 + count_zeros(n//10)
    return count_zeros(n//10)
n = 918200007302730303800
print(count_zeros(n))