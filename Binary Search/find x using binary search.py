def binary_search(l,x):
    left=0
    right=len(l)-1
    while left<=right:
        mid= (left+right)//2
        if l[mid]==x:
            return mid
        elif l[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return -1

l = [-1,0,2,3,5,8,10]
find = 7

print(binary_search(l,find))
            
    