from collections import Counter

class SmallestSubstring:
    def __init__(self, str1, pattern):
        self.str1 = str1
        self.pattern = pattern

    def find_smallest_substring(self):
        start = 0
        min_length = float('inf')
        char_frequency = Counter(self.pattern)

        for end in range(len(self.str1)):
            right_char = self.str1[end]

            if right_char in char_frequency:
                char_frequency[right_char] -= 1

            while len(char_frequency) == 0:
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    matched = self.str1[start:end+1]

                left_char = self.str1[start]
                if left_char in char_frequency:
                    char_frequency[left_char] += 1

                if char_frequency[left_char] > 0:
                    del char_frequency[left_char]

                start += 1

        return matched if min_length != float('inf') else ""

if __name__ == '__main__':
    str1 = "abdbca"
    pattern = "abc"

    smallest_substring_finder = SmallestSubstring(str1, pattern)
    result = smallest_substring_finder.find_smallest_substring()
    print(result)
