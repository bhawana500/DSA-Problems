def binary_search(l,x):
    left = 0
    right = len(l) - 1
    while(left <= right):
        mid=(left+right)//2
        
        if l[mid] == x and (mid==0 or l[mid-1] == 0):
            return mid
        elif l[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
 
l = [0,0,0,0,1,1,1,1,1,1,1,1,1,1]


print(binary_search(l,1))