s1 = '{}{})'
s2 = '({}((){}))'

def check_parenthesis(s):
    if len(s)==0:
        return 
    left_paren = ["(", "{","["]
    right_paren =  [ ")", "}", "]"]
    stack =[]
    for i in s:
        if i in left_paren:
            stack.append(i)
        elif i in right_paren:
            pos = right_paren.index(i)
            if len(stack)==0 or (left_paren[pos]!=stack[len(stack)-1]):
                return False
            else:
                stack.pop()

    if len(stack)==0:
        return True
    else:
        return False
    
def main():
    print(check_parenthesis(s1))
    print(check_parenthesis(s2))

main()
