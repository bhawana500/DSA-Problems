def sum_of_digits(n):
    if n == 1:
        return 1
    return n + sum_of_digits(n-1)
print(sum_of_digits(10))