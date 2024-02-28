matrix = [
    [1,1,0,0],
    [1,0,0,1],
    [0,1,1,1],
    [1,0,1,0]
]

def find_an_invert_image(matrix):
    c = len(matrix)
    for row in matrix:
        print("row: ", row)
        for i in range((c+1)//2):
            print("i: ",i)
            row[i],row[c-i-1] = row[c-i-1]^1 , row[i]^1
            print("row1: ",row)

    return matrix

print(find_an_invert_image(matrix))