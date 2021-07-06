# Input: String="abdbca", Pattern="abc"
# Output: "bca"
# Explanation: The smallest substring having all characters of the pattern is "bca".
from collections import Counter
str1 = "abdbca"

pattern = "abc"

matched = ""

start =0
min_length =0


char_frequency = Counter(pattern)

for end in range(len(str1)):
    right_char = str1[end]
    
    if right_char in char_frequency:
        char_frequency[right_char]-=1
    min_length+=1
    if len(char_frequency)==0:
        min_length = min(min_length,end-start+1)
        
        
        
        
        
        
        
    
    
    