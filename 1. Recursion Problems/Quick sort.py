def partition(l,si,ei):
    if len(l)==1 or len(l)==0:
        return
    count=0
    for i in range(si,ei+1):
        if l[si]>l[i]:
            count+=1
    mid=si+count
    temp=l[si]
    l[si]=l[mid]
    l[mid]=temp
    
    i = si
    j = ei
    while i<mid and j > mid:
        if l[i] < l[mid]:
            i+=1
        elif l[j] >= l[mid]:
            j -=1
        else:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
    return mid

def q_sort(l,si,ei):
    if si>ei:
        return
    mid = partition(l,si,ei)
    q_sort(l,si,mid-1)
    q_sort(l,mid+1,ei)
    
l=[3,7,4,2,8,5,6,1,9]   

q_sort(l,0,len(l)-1) 
print(l)

