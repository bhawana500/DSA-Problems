def min_capacity(weights,d):
    left = max(weights)
    max_capacity=0
    for i in weights:
        max_capacity+=i
    right = max_capacity
    
    while left<=right:
        mid = (left+right)//2
        load=0
        day=1
        for i in weights:
            if load+i>mid:
                load=i
                day+=1
            else:
                load+=i
        
        if day <= d:
            right = mid-1
            capacity = mid
        else:
            left = mid+1
    return capacity

weights = [1,2,3,4,5]

print(min_capacity(weights,3))
