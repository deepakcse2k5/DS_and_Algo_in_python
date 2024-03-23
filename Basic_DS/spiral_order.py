matrix = [[2,6,8],[3,7,10],[5,8,11]]

def spiral_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, -1
    result = []
    direction =1
    while rows >0 and cols >0:
        for _ in range(cols):
            col += direction
            result.append(matrix[row][col])
        rows -= 1
        for _ in range(rows):
            row += direction
            result.append(matrix[row][col])
        cols -= 1
        direction *= -1
    return result


print(spiral_order(matrix))


# Time complexity: O(m*n), where m is the number of rows and n is the number of columns in the matrix.

# Space complexity: O(1) since we are not using any additional data structures for storing the intermediate results.
