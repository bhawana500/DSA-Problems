# Agnostic means We don't know whether the Array is sorted in Ascending or Descending Array


def binary_search(l,x):
    left=0
    right=len(l)-1
    if l[0] > l[1]:
        while left<=right:
            mid= (left+right)//2
            if l[mid]==x:
                return mid
            elif l[mid] < x:
                right = mid-1
            else:
                left = mid + 1
    else:
        while left<=right:
            mid= (left+right)//2
            if l[mid]==x:
                return mid
            elif l[mid] < x:
                left = mid+1
            else:
                right = mid-1
    return -1

l = [12,9,8,7,4,2,0,-1,-9]
m=[1,2,3,4,5,6,7,8,910]
find = 4

print(binary_search(m,find))
print(binary_search(l,find))
            
    