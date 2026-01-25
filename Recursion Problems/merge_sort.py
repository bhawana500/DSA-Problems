def merge(l,l1,l2):
    i = 0
    j = 0
    k = 0
    while i < len(l1) and j < len(l2):
        
        if l1[i] < l2[j]:
            l[k] = l1[i]
            i+=1
            k+=1
        else:
            l[k] = l2[j]
            j+=1
            k+=1
    while i<len(l1):
        l[k] = l1[i]
        i+=1
        k+=1
    while j < len(l2):
        l[k] = l2[j]
        j+=1
        k+=1
def sort1(l):
    if len(l)==0 or len(l)==1:
        return
    mid=len(l)//2
    l1 = l[:mid]
    l2 = l[mid:]            
    sort1(l1)
    sort1(l2)
    merge(l,l1,l2)
l=[10,1,5,8,9,2,5,3]
sort1(l)
print(l)