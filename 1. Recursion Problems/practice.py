def binary_search(l,mx,t):
    large = 0
    left = 0
    right = len(l)-1
    if l[0] < l[-1]:
        return 0
    while left <= right:
        mid = (left+right)//2
        if l[mid] == mx:
            large = mid
            left = mid+1
        elif l[mid] < l[0]:
            right = mid-1
        else:
            left = mid+1
    if l[0] <= t:
        left = 0
        right = large
    else:
        left = large+1
        right = len(l)-1
    while left<=right:
        mid = (left+right)//2
        if l[mid] == t:
            return mid
        elif l[mid] < t:
            left = mid+1
        else:
            right = mid-1
    return -1
        

l = [6,7,8,9,12,34,56,78,90,4,5,5,6]
print(binary_search(l,90,12))