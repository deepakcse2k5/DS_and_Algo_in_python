# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".


str1 = "cbbebi"
k=3


def longest_substring_with_k_distinct(str1,k):
    
    start=0
    max_length =0

    char_frequency = {}
    if len(str1)<k:
        return str1
    
    for end  in range(len(str1)):
        right_char=str1[end]
        if right_char not in char_frequency:
            char_frequency[right_char]=0
            print("char frequency1:",char_frequency)
        char_frequency[right_char]+=1
        print("char frequency:",char_frequency)
            
        while len(char_frequency)>k:
            left_char = str1[start]
            char_frequency[left_char]-=1
            if char_frequency[left_char]==0:
                del char_frequency[left_char]
            start+=1
        max_length = max(max_length,end-start+1)
    return max_length

print(longest_substring_with_k_distinct(str1,k))


        
    
    
    
    