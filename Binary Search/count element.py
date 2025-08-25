def f(l,x):
    left = 0
    right = len(l)-1
    first = -1
    while left<=right:
        mid = (left+right)//2
        if x == l[mid]:
            first = mid
            right = mid-1
        elif x > l[mid]:
            left = mid+1
        else:
            right = mid-1
    return first
def la(l,x):
    left = 0
    right = len(l)-1
    first = -1
    while left<=right:
        mid = (left+right)//2
        if x == l[mid]:
            first = mid
            left = mid+1
        elif x > l[mid]:
            left = mid+1
        else:
            right = mid-1
    return first
l = [1,2,3,4,5,5,5,5,5,6,7,8,9]
print(la(l,5) - f(l,5) +1)
    