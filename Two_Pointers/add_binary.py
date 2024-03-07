str1 = "10"
str2 = "11"


def add_binary(str1, str2):
    result = []
    carry = 0

    ptr1 = len(str1) - 1
    ptr2 = len(str2) - 1

    while ptr1 >= 0 or ptr2 >= 0:
        if ptr1 >= 0:
            digit1 = ord(str1[ptr1]) - ord('0')
        else:
            digit1 = 0

        if ptr2 >= 0:
            digit2 = ord(str2[ptr2]) - ord('0')
        else:
            digit2 = 0

        total_sum = digit1 + digit2 + carry
        current_digit = total_sum % 2
        carry = total_sum // 2

        result.append(current_digit)

        ptr1 -= 1
        ptr2 -= 1

    if carry:
        result.append(carry)

    reversed_result = result[::-1]
    binary_sum = ''.join(str(digit) for digit in reversed_result)

    return binary_sum


# print(add_binary(str1, str2))

def main():
    str1_list = ["1100", "1010100", "10101", "1111", "10101100110010101"]
    str2_list = ["0011", "0100011", "01010", "11111", "1011001010110010100"]

    for i in range(len(str1_list)):
        print(str(i + 1) + ".\tFirst input string:  ", str1_list[i])
        print("\tSecond input string: ", str2_list[i])

        print("\tBinary Sum:          ", add_binary(str1_list[i], str2_list[i]))
        print('-' * 100);


if __name__ == '__main__':
    main()

# Time complexity
# The time complexity of this solution is O(max(n,m)),
# where n and m are the lengths of strings str1 and str2 respectively.
# This is because the loop will run until the longest string has been traversed.

# Space complexity
# The space complexity of this solution is O(max(n,m)), since we are using result to store the binary sum.
