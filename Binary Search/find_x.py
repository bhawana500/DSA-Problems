def binary_search(l,target,li,si):
    mid=(li+si)//2
    if li>si:
        return -1
    if target==l[mid]:
        return mid
    elif target>l[mid]:
        return binary_search(l,target,mid+1,si)
    else:
        return binary_search(l,target,li,mid-1)

l=[-9,0,1,3,6,9,12,56,78]                                             
print(binary_search(l,12,0,len(l)-1))