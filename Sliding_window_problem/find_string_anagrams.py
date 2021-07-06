# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
str1 = "abbcabc"
pattern = "abc"

def find_string_anagrams(str1,pattern):
    result_indexes =[]
    start = 0
    matched =0
    char_frequency = {}
    
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char]=0
        char_frequency[char]+=1
        
    for end in range(len(str1)):
        right_char = str1[end]
        if right_char in char_frequency:
            char_frequency[right_char] -=1
            if char_frequency[right_char]==0:
                matched +=1
        if matched == len(char_frequency):
            result_indexes.append(start) 
            
        if end >= len(pattern)-1:
            left_char = str1[start]
            start+=1
            if left_char in char_frequency:
                if char_frequency[left_char]==0:
                    matched -=1
                char_frequency[left_char]+=1
    return result_indexes


print(find_string_anagrams(str1,pattern))