def binary_search(l,x):
    left = 0
    right = len(l)-1
    last = -1
    while(left<=right):    # wite the condition which is true   .....not false
        mid = (left+right)//2
        if l[mid] == x:
            last = mid+1
            left = mid+1
        elif l[mid] < target:
            left = mid+1
        else:
            last = mid
            right = mid-1
    return last

l = [1,3,4,4,4,4,5,6,7,9]
target = 4
print(binary_search(l,target))