def str_to_int(s, si, ei):
    if si>ei:
        return ""
    elif s[0] == '0':
        print("hi")
        return str_to_int(s[1:],si+1,ei)
    return s[si] + str_to_int(s, si+1, ei)

n = "0090"
print(str_to_int(n,0,len(n)-1))