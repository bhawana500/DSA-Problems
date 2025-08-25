def partition(l,si,ei):
    if len(l)==1 or len(l)==0:
        return
    count=0
    for i in range(len(l)):
        if l[0]>l[i]:
            count+=1
    mid=si+count
    temp=l[0]
    l[0]=l[mid]
    l[mid]=temp
    for i in range(len(l[:mid])):
        for j in range(len(l[mid+1:])):
            if l[i]>l[mid] and l[i]>l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
            break
    return l
def q_sort(l,si,ei):
    if len(l)==1 or len(l)==0:
        return
    l=l[si:ei+1]
    mid = partition(l,si,ei)
    if mid==None:
        return
    q_sort(l,si,mid-1)
    q_sort(l,mid+1,ei)
l=[3,7,4,2,8,5,6,1,9]   
l=partition(l,0,len(l)-1) 
print(l)
