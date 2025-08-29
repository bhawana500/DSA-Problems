def binary_search(l,target):
    left = 0
    right = len(l)-1
    
    while left<=right:
        mid = (left+right)//2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            if target == l[mid-1]:
                right = mid-1
            else:
                left = mid+1
        else:
            if target == l[mid+1]:
                left = mid+1
            else:
                right = mid-1
    return -1

l = [2,1,4,3,6,5,9,7,10,12,11]
print(binary_search(l,6))
                        