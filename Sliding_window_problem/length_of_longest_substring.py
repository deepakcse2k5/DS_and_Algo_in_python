# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".


str1 = "aabccbb"
k=2


def length_of_longest_substring(str1,k):
    start =0
    max_length =0
    char_frequency = {}
    max_repeat_count =0
    for end in range(len(str1)):
        right_char = str1[end]
        if right_char not in char_frequency:
            char_frequency[right_char]=0
        char_frequency[right_char]+=1
        max_repeat_count = max(max_repeat_count,char_frequency[right_char])
        if (end-start+1-max_repeat_count)>k:
            left_char = str1[start]
            char_frequency[left_char]-=1
            start+=1
        max_length = max(max_length,end-start+1)
    return max_length


print(length_of_longest_substring(str1,k))

            
            
            
        
    
    
    
    