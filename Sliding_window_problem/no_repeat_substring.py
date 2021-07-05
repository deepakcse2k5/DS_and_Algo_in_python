# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

str1 = "abccde"


def no_repeat_substring(str1):
    start =0
    max_length =0
    char_frequency =set()
    
    for end in range(len(str1)):
        right_char = str1[end]
        if right_char  in char_frequency:
            max_length = max(max_length, end-start)
            start = end 
        else:
            char_frequency.add(right_char)
    return max_length

print(no_repeat_substring(str1))
            

