def find_sqrt(n,N):
    left = 0
    right = n
    answer = -1
    while left<=right:
        mid = (left+right)//2
        if mid**N <= n:
            answer = mid
            left = mid+1
        else:
            right = mid-1
    return answer
N=9
n = 400

a = find_sqrt(n,N)
print(a)