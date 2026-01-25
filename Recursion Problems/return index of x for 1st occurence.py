def check_list(x,l,start):
    if start == len(l):
        return False
    if l[start] == x:
        return start
    else:
        return check_list(x,l,start+1)
l=[1,2,3,4,2,5,7,6,7,8]
x=int(input("Enter the element to find it's first occurence: "))
print(check_list(x,l,0))