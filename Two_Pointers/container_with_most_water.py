height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def container_with_most_water(height):
    start = 0
    end = len(height) - 1
    max_area = 0
    while start < end:
        width = end - start
        h = min(height[start], height[end])
        max_area = max(max_area, width * h)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return max_area


if __name__ == '__main__':
    print(container_with_most_water(height))
# Time complexity
# The time complexity of this solution is O(n), where n is the length of the input list height. This is because we only iterate through the list once, using two pointers to traverse the list from both ends.

# Space complexity
# The space complexity of this solution is O(1). We are only using a few variables to store the maximum area and the two pointers, and not using any data structures that grow with the input list height.
