def binary_search(arr,target):
    left = 0
    right = len(l)-1

    while left<=right:
        mid  = (left+right)//2

        if arr[mid] == target:
            return mid

        elif left<mid and arr[mid-1] == target:
            return mid-1
        else:
            if right>mid and arr[mid+1] == target:
                return mid+1
        if arr[mid]<target:
            left = mid+1
        else:
            right=mid-1

l = [2,1,4,3,6,5,9,7,10,12,11]
print(binary_search(l,6))
