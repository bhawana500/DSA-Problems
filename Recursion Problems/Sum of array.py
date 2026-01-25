def sum_array(l):
    k=len(l)
    if k==0:
        return 0
    return l[-1] + sum_array(l[:k-1])

term=int(input("Enter the Number of terms in list: "))
l=[]
for i in range(term):
    element=int(input("Enter the elements of a list: "))
    l.append(element)
print("Your list is =>",l)
print("Sum of the list is",sum_array(l))