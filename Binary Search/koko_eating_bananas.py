# Koko Eating Bananas
# Banana piles = [3, 6, 7, 11]
# Hours = 8

# Koko eats k bananas per hour
# Try k = 4 
# 3 → 1 hour
# 6 → 2 hours
# 7 → 2 hours
# 11 → 3 hours    ceil value
# Total = 8 hours ✅       
# So minimum speed = 4

# my idea:
#             for bananas in piles:
#             # if bananas%mid == 0:
#             #     hours+=bananas//mid
#             # else:
#             #     hours += bananas//mid+1

def min_time(piles,h):
    left = 1
    right = max(piles)
    
    while left<=right:
        mid = (left+right)//2
        hours = 0
        
        for bananas in piles:
            hours += (bananas+mid-1)//mid
        
        if hours > h:
            left = mid+1
        else:
            right = mid-1
            
    return left

l = [3,6,7,8]
h=10
min_banana_per_hour = min_time(l,h)
print(min_banana_per_hour)



# my logic
