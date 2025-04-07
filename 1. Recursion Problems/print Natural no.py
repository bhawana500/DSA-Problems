def naturalNo(n):
    if n==0:
        return
    print(n)
    naturalNo(n-1)
    return
n=int(input("Enter a number: "))
naturalNo(n)