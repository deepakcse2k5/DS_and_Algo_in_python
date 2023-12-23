def is_palin_perm(s1):
    s1 = s1.replace(" ","").lower()
    
    d = dict()
    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            
    odd_count =0
    for k,v in d.items():
        if v%2!=0 and odd_count==0:
            odd_count+=1
        elif v%2!=0 and odd_count!=0:
            return False
    return True

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))
            
         