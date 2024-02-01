class LongestPalindromicSubstring:
    def __init__(self, str1):
        self.str1 = str1

    def longest_palindromic_string(self):
        result = ""
        result_length = 0

        for i in range(len(self.str1)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(self.str1) and self.str1[l] == self.str1[r]:
                if (r - l + 1) > result_length:
                    result = self.str1[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(self.str1) and self.str1[l] == self.str1[r]:
                if (r - l + 1) > result_length:
                    result = self.str1[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1

        return result


if __name__ == '__main__':
    str1 = "babad"
    palindrome_calculator = LongestPalindromicSubstring(str1)
    result = palindrome_calculator.longest_palindromic_string()
    print(result)
