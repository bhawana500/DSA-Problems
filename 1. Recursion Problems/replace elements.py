def replace(s,a,b,start):
    if start==len(s):
        return s
    if s[start]==a:
        s = s[:start] + b + s[start+1:]
    return replace(s,a,b,start+1)
s='hallo haa'
a=input("Enter the element you have to change: ")
b=input("Enter the element you have to place: ")
print(replace(s,a,b,0))