s1 = '{}[]{}[{}])'

def valid_parentheis(s1:str)-> bool:
    #edge case
    if len(s1)==0:
        return True
    stack = []
    hash_map = {')':'(','}':'{',']':'['}
    for char in s1:
        if char not in hash_map:
            stack.append(char)
        else:
            if stack:
                popped_element = stack.pop()
            else:
                popped_element = '*'
            if hash_map[char]!=popped_element:
                return False
    return not stack
        

print(valid_parentheis(s1))


# Time complexity - O(n), where n is the no of character in input string

# Space Complexity - O(n) , where n is the space required for stack



