def naturalNo(n):
    if n==0:
        return
    naturalNo(n-1)
    print(n)
    return
n=int(input("Enter a number: "))
naturalNo(n)