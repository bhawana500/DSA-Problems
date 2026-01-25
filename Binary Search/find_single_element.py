# my LOGIC
# def single_element(l):
#     left = 0
#     right = len(l) - 1
#     while(left<=right):
#         mid = (left+right) // 2
#         if l[mid] != l[mid+1] and l[mid] != l[mid-1]:
#             return mid
#         elif (mid%2==0 and l[mid]==l[mid+1]) or (mid%2!=0 and l[mid]==l[mid-1]):
#             left = mid+1
#         else:
#             right = mid-1
#     return -1

# taken

def single_element(l):
    left = 0
    right = len(l)-1
    while(left<right):
        mid = (left+right)//2
        if mid%2 != 0:
            mid-=1
        if l[mid] == l[mid+1]:
            left = mid+2
        else:
            right = mid
    return left
                


l = [1,1,2,2,3,3,5,5,6]

print(single_element(l))
    