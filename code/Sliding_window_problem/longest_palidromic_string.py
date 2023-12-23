str1 = "babad"

def longest_palindromic_string(str1):
    result = ""
    result_length =0
    for i in range(len(str1)):
        # odd length
        l,r =i,i
        while l>=0 and r<len(str1) and str1[l]==str1[r]:
            if (r-l+1)>result_length:
                result = str1[l:r+1]
                result_length = r-l+1
            l-=1
            r+=1
        # even length
        l,r = i,i+1
        while l>=0 and r<len(str1) and str1[l]==str1[r]:
            if (l-r+1)> result_length:
                result = str1[l:r+1]
                result_length = r-l+1
            l-=1
            r+=1
    
    return result
            
    

    
print(longest_palindromic_string(str1))
    