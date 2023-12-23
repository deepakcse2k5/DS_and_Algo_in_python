def reverse(strng):
    if strng=="":
        return ""
    else:
        return reverse(strng[1:]) + strng[0]
        
strng ="python"

print(reverse(strng))




              
              