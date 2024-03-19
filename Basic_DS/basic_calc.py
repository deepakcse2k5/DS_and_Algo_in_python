exp = "12 - (6 + 2) + 5"


def basic_calc(exp):
    exp = exp.replace(" ","")
    stack = []
    current_num = 0
    sign = 1

    result = 0
    for i in range(len(exp)):
        if exp[i].isdigit():
            current_num = current_num * 10 + int(exp[i])
        elif exp[i] in ["-", "+"]:
            result += sign * current_num
            current_num = 0
            sign = -1 if exp[i] == "-" else 1
        elif exp[i] == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif exp[i] == ")":
            result += sign * current_num
            current_num = 0
            result *= stack.pop()
            result += stack.pop()
    result += sign * current_num
    return result

print(basic_calc(exp))
