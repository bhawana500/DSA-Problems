def min_of_max(l,s):
    if len(l)<s:
        return -1
    left = max(l)
    right = 0
    for i in l:
        right+=i
    ans=-1
    
    while left<right:
        mid = (left+right)//2
        count_s=1
        last=0
        
        for i in range(0,len(l)):
            if l[i]+last <= mid:
                last+=l[i]
            else:
                count_s+=1
                last=l[i]
                
        if count_s<=s:
            right = mid-1
            ans = mid
        elif count_s>s:
            left = mid+1
    return ans
l = [25,46,28,49,24]
s = 4
print(min_of_max(l,s))
        
        