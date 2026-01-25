def single_element(l):
    left = 0
    right = len(l)-1
    while(left>right):
        mid = (left+right)//2
        if mid%2 != 0:
            mid-=1
        if l[mid] == l[mid+1]:
            left = mid+2
        else:
            right = mid
    return l[left]
                


l = [1,1,2,2,3,3,5,5,6]

print(single_element(l))
    