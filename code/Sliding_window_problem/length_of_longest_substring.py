class LongestRepeatingSubstring:
    def __init__(self, str1, k):
        self.str1 = str1
        self.k = k

    def length_of_longest_substring(self):
        start = 0
        max_length = 0
        char_frequency = {}
        max_repeat_count = 0

        for end in range(len(self.str1)):
            right_char = self.str1[end]

            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            max_repeat_count = max(max_repeat_count, char_frequency[right_char])

            if (end - start + 1 - max_repeat_count) > self.k:
                left_char = self.str1[start]
                char_frequency[left_char] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

if __name__ == '__main__':
    str1 = "aabccbb"
    k = 1

    substring_calculator = LongestRepeatingSubstring(str1, k)
    result = substring_calculator.length_of_longest_substring()
    print(result)
