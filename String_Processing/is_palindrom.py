def is_palindrom(s):
    i = 0
    j = len(s) -1
    
    while i<j:
        while not s[i].isalnum() and i<j:
            i+=1
        while not s[j].isalnum() and i<j:
            j-=1
        if s[i].lower() != s[j].lower():
            return False
        
        i+=1
        j-=1
    return True

s = "was it a cat i saw it"

print(is_palindrom(s))