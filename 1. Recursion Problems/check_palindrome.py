def is_palindrome(s,si,ei):
    
    if si>ei:
        return True
    elif s[si] != s[ei]:
        return False
    return is_palindrome(s,si+1,ei-1)

s = "abcba"
print(is_palindrome(s,0,len(s)-1))