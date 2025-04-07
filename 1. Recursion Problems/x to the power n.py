def pow(x,n):
    if n==1:
        return x
    return x * pow(x,n-1)
x=int(input("Enter the Base Value: "))
n=int(input("Enter the Power of the Base: "))
print(f"{x} to the power {n} is {pow(x,n)}")