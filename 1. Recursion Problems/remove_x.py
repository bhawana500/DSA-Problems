def remove(s,x):
    if len(s)==0:
        return s
    if s[0]=='x':
        return '' + remove(s[1:],x)
    else:
        return s[0] + remove(s[1:],x)
s='xyxyxyxyxyxy'
print(remove(s,'x'))