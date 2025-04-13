def find(l,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if l[mid]==x:
        return mid
    if l[mid]>x:
        return find(l,x,si,mid-1)
    else:
        return find(l,x,mid+1,ei)
l=[1,2,3,4,5,6,7,8,22,44,56,88,100,2,9,10,1]
x=3
l.sort()
print(l)
print(f"{x} index is",find(l,x,0,len(l)-1)) 