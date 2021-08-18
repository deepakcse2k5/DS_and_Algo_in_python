

def isPalindrome(strng):
    if strng=="":
        return True
    elif strng[0]!=strng[-1]:
        return False
    else:
        return isPalindrome(strng[1:-1])
    
    
print(isPalindrome("welcome"))


print(isPalindrome("sas"))