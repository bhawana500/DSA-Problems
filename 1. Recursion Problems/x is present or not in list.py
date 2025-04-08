def find_x(x,l):
    k=len(l)
    if k==0:
        return False
    if x == l[k-1]:
        return True
    else:
        return find_x(x,l[:k-1])
l=[1,2,3,4,5,6,7,8,9,10]
x=int(input("Enter the number to find in the given List: "))
print(find_x(x,l))