def check_list(l):
    k=len(l)
    if k==0:
        return 'List is Empty'
    if k==1:
        return True
    if l[k-1]>=l[k-2]:
        return check_list(l[:k-1])
    else:
        return False
l=[2,2,5,3,7,7,9]
print(check_list(l))