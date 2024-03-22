tokens = ["2", "5", "*", "4", "+","3","2", "*","1","+", "/"]

def reverse_polish_notation(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "*":
                result = num1 * num2
            else:
                result = num1 / num2
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()

print(reverse_polish_notation(tokens))



# Time complexity: O(n),where n is the number of elements in the input tokens.
# Space complexity: O(n), where n is the space required by stack.