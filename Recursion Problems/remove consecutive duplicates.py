def remove(s):
    if len(s)==1:
        return s
    if s[0] == s[1]:
        return remove(s[1:])
    else:
        return s[0] + remove(s[1:])
s='aabbccddaabbccdd'    
print(remove(s))
    
