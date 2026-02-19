def min_div(arr,h):
    left = 1
    right = max(arr)
    
    while left<=right:
        mid = (left+right)//2
        sum = 0
        
        for ele in arr:
            sum += (ele+mid-1)//mid
        
        if sum > h:
            left = mid+1
        else:
            right = mid-1
            
    return left

l = [2,3,4,5,6,7,8]
h=10
min_divisor = min_div(l,h)
print(min_divisor)
