

def happy_number(number):
    slow = number//10
    fast = number % 10
    num_list =[]
    def check_number(slow,fast):
        sum = slow**2 + fast **2
        print(sum)
        if sum in num_list:
            return "Not happy Number"
        elif sum ==1:
            return "happy Number"
        else:
            num_list.append(sum)
        slow = number//10
        fast = number % 10
        return check_number(slow,fast)
    return check_number(slow,fast)
    
print(happy_number(23))
            