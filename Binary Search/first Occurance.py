def binary_search(l,x):
    left=0
    right=len(l)-1
    first = -1
    while left<=right:
        mid= (left+right)//2
        if l[mid]==x:
            first= mid
            right = mid-1
        elif l[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return first


m=[1,2,4,4,4,4,4,4,5,6,7,8,910]
find = 4

print(binary_search(m,find))

            
    
            
    