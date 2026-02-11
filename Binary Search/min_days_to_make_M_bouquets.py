def make_bouquets(l,f,m):
    left = min(l)
    right = max(l)
    ans = -1
    while left <= right:
        mid = (left+right)//2
        n = 0
        bouquets = 0
        
        for i in l:
            if i <= mid:
                n+=1   
            else:
                n=0
            if n==f:
                bouquets += 1 
                n=0
        
        if bouquets < m:
            left = mid+1
        else:
            ans = mid
            right = mid-1
    return ans

bloom_day = [7,7,7,7,13,50,67,2,3,4,1,4,5,6]
m = 2
f = 3
print(make_bouquets(bloom_day,f,m)) 
            
    
    