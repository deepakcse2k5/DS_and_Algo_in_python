# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Time Complexity O(N+M) and Space Complexity O(M) where N and M are the number of elements in string and pattern

str1 = "oidbcaf"
pattern = "abc"


def find_permutation(str1, pattern):
    start = 0
    matched = 0
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    for end in range(len(str1)):
        right_char = str1[end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        if matched == len(char_frequency):
            return True
        if end >= len(pattern) - 1:
            left_char = str1[start]
            start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False


print(find_permutation(str1, pattern))
