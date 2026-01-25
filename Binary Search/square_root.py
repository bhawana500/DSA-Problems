def find_sqrt(n):
    left = 0
    right = n
    answer = -1
    while left<=right:
        mid = (left+right)//2
        if mid*mid <= n:
            answer = mid
            left = mid+1
        else:
            right = mid-1
    return answer

n = 29

a = find_sqrt(n)
print(a)