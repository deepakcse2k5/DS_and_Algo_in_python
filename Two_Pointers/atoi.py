s = "79"


def atoi(s):
    result = 0
    sign = 1
    i = 0
    # edge case
    if len(s) == 0:
        return 0
    s = s.lstrip()
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1
    while i < len(s) and '0' <= s[i] <= '9':
        digit = ord(s[i]) - ord('0')
        if result > (2 ** 31 - 1 - digit) // 10:
            return sign * (2 ** 31 - 1) if sign == 1 else sign * (2 ** 31)
        result = result * 10 + digit
        i += 1
    return sign * result


def main():
    input_strings = ["25", "   -25", "999 with words", "words and 567", "-91283472332", "91283472332"]

    for i in range(len(input_strings)):
        print(i + 1, ".\tInput string     : ", end="")
        print('"{0}"'.format(input_strings[i]))

        stoi = atoi(input_strings[i])

        print("\tConverted integer: ", stoi)
        print("-" * 100)


if __name__ == '__main__':
    main()

# Time complexity
# The time complexity of this solution is O(n), where n
# is the length of the input string s. This is because we iterate through the input string once,
# character by character, without nested loops or recursive calls.
#
# Space complexity
# The space complexity of this solution is O(1).
