colors = [0, 1, 0, 1, 2, 1, 2]


def sort_colors(colors):
    start = 0
    end = len(colors) - 1
    i = 0
    while i <= end:
        if colors[i] == 0:
            colors[i], colors[start] = colors[start], colors[i]
            start += 1
            i += 1
        elif colors[i] == 2:
            colors[i], colors[end] = colors[end], colors[i]
            end -= 1
        else:
            i += 1
    return colors


print(sort_colors(colors))

# Time complexity
# The time complexity of this solution is O(n) since we’re only traversing the array once.

# Space complexity
# The space complexity of this solution is  O(1) since no extra space is used.
