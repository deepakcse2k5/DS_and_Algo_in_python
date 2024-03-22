heights = [2, 4, 5, 7, 3, 9]

def largest_rectangle(heights):
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        while stack[-1]!=-1 and heights[stack[-1]]>= heights[i]:
            curr_height = heights[stack.pop()]
            right_boundary = i
            left_boundary = stack[-1]
            curr_width = right_boundary- left_boundary -1
            curr_area = curr_height * curr_width
            max_area = max(max_area, curr_area)
        stack.append(i)
    n = len(heights)
    while stack[-1]!=-1:
        curr_height = heights[stack.pop()]
        left_boundary = stack[-1]
        curr_width = n - left_boundary-1
        curr_area = curr_height * curr_width
        max_area = max(max_area, curr_area)
    return max_area

print(largest_rectangle(heights))


# Time complexity
# The time complexity of this solution is O(n), where n is the number of bars in the histogram. This is because n indices are pushed into and popped from the stack.

# Space complexity
# The space complexity of this solution is O(n), since a stack is used, where n indices are pushed to it.


