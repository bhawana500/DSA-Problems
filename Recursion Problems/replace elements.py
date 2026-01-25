def change(s,a,b):
    if len(s)==0:
        return s
    if s[0]==a:
        return b + change(s[1:],a,b)
    else:
        return s[0] + change(s[1:],a,b)
s='aaaaaabhiijaaa'
print(change(s,'a','b'))