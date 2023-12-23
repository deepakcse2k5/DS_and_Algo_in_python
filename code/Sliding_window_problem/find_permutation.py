class PermutationChecker:
    def __init__(self, str1, pattern):
        self.str1 = str1
        self.pattern = pattern

    def check_permutation(self):
        start = 0
        matched = 0
        char_frequency = {}

        for char in self.pattern:
            char_frequency[char] = char_frequency.get(char, 0) + 1

        for end in range(len(self.str1)):
            right_char = self.str1[end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched += 1

            if matched == len(char_frequency):
                return True

            if end >= len(self.pattern) - 1:
                left_char = self.str1[start]
                start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return False


if __name__ == '__main__':
    str1 = "oidbcaf"
    pattern = "abc"

    checker = PermutationChecker(str1, pattern)
    result = checker.check_permutation()
    print(result)
