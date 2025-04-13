def find(l,x,si,ei):
    if si>ei:
        return -1
    k=(si+ei)//2
    if l[k]==x:
        return k
    if l[k]>x:
        return find(l,x,si,k-1)
    else:
        return find(l,x,k+1,ei)
l=[1,2,3,4,5,6,7,8,22,44,56,88,100,2,9,10,1]
x=1001
l.sort()
print(l)
print(find(l,x,0,len(l)-1)) 