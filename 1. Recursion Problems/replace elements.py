def exchange(s,a,b):
    if len(s)==0:
        return s
    if s[0]==a:
        return b + exchange(s[1:],a,b)
    else:
        return s[0] + exchange(s[1:],a,b)
s='aaaaaabhiijaaa'
print(exchange(s,'a','b'))