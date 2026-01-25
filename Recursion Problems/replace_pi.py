# In this problem if 'PI' is found then exchange it to 3.14 
def replace(s):
    if len(s)==0:
        return s
    if s[:2] == 'pi':
        return '3.14' + replace(s[2:])
    else:
        return s[0] + replace(s[1:])
s='hellopihiipinopiPI'
s=s.lower()
print(replace(s))