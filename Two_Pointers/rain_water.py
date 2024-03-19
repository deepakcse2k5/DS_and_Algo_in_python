heights = [3,1,0,2,1]

def rain_water(heights):
    left = 0
    right = len(heights) - 1
    left_max = 0
    right_max = 0
    result = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                result += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                result += right_max - heights[right]
            right -= 1
    return result


def main():
    input_list = [
        [1, 0, 1, 2, 1, 4, 0, 3, 5],
        [2, 0, 9, 6],
        [3, 1, 2, 0, 2],
        [4, 2, 5, 3], [3, 0]

    ]
    index = 1
    for i in input_list:
        print(str(index) + ".\tHeights: " + str(i))
        print("\tMaximum rainwater: " + str(rain_water(i)))
        index += 1
        print("-" * 100)


if __name__ == "__main__":
    main()


# Time complexity
# The time complexity of this solution is O(n) where n is the number of elements in the heights array.
#
# Space complexity
# Since no extra space is being used, the space complexity for this solution is constant O(1).