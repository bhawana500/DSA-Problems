def find_peak(l):
    left = 0
    right = len(l) - 1
    while left < right:
        mid = (left+right)//2
        if l[mid] < l[mid+1]:
            left = mid+1
        else:
            right = mid
    return left

l = [1,2,1,3,4,5,6,5,1]
print(find_peak(l))