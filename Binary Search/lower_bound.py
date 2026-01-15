def binary_search(l,x):
    left = 0
    right = len(l)-1
    result = -1
    while(left<=right):    # wite the condition which is true   .....not false
        mid = (left+right)//2
        if l[mid] >= x:
            right = mid-1
            result = mid
        else:
            left = mid+1
    return result

l = [1,3,4,4,4,5,6,7,9]
target = 4
print(binary_search(l,target))