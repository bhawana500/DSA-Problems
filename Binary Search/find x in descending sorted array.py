def binary_search(l,x):
    left=0
    right=len(l)-1
    while left<=right:
        mid= (left+right)//2
        if l[mid]==x:
            return mid
        elif l[mid] < x:
            right = mid-1
        else:
            left = mid + 1
    return -1

l = [12,9,8,7,4,2,0,-1,-9]
find = 0

print(binary_search(l,find))
            
    