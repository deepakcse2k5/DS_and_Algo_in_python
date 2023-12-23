class LongestSubstringWithKDistinct:
    def __init__(self, str1, k):
        self.str1 = str1
        self.k = k

    def find_longest_substring(self):
        start = 0
        max_length = 0
        char_frequency = {}

        if len(self.str1) < self.k:
            return self.str1

        for end in range(len(self.str1)):
            right_char = self.str1[end]

            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1

            while len(char_frequency) > self.k:
                left_char = self.str1[start]
                char_frequency[left_char] -= 1

                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]

                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length


if __name__ == '__main__':
    str1 = "cbbebi"
    k = 3

    longest_substring_calculator = LongestSubstringWithKDistinct(str1, k)
    result = longest_substring_calculator.find_longest_substring()
    print(result)
