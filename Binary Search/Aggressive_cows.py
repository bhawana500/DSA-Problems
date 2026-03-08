def max_of_min_distances(l,cows):
    left = 1
    right = l[-1]-l[0]
    ans = -1
    
    while left<=right:
        mid = (left+right)//2
        
        count_cows=1
        last=l[0] 
        for i in range(1,len(l)):    
            
            if l[i]-last >= mid:  #  for min of max use <=
                count_cows+=1
                last=l[i]
        
        if count_cows>=cows:
            ans=mid
            left=mid+1
        else:
            right = mid-1     
    return ans

consecutive_cows_distance=[0,3,5,7,9,10,17]
cows = 4
print(max_of_min_distances(consecutive_cows_distance,cows))
        