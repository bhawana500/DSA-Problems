# # DIFF APPROach
# def k_num(l,k):
#     left = 1
#     right = l[-1] + k
#     ans=-1
#     while(left<=right):   # AGAIN WRITE CONDITION IN WHICH IT WORKS!!
#         mid=(left+right)//2
        
#         count=0
#         for i in l:
#             if i<=mid:
#                 count+=1
#             missing = mid-count

#         if missing==k:
#             return mid
#         elif missing < k:
#             left = mid+1
#         else:
#             right = mid-1
#     return ans
            
# l=[2,3,4,7,11]
# k=5
# print(k_num(l,k))


# BEST APPROACH
def k_num(l,k):
    left=0
    right = len(l)-1
    while left<=right:
        mid = (left+right)//2
        
        missing = l[mid] -(mid+1)
        
        if missing<k:
            left=mid+1
        else:
            right = mid-1
    return left+k
l=[2,3,4,7,11]
k=5
print(k_num(l,k))