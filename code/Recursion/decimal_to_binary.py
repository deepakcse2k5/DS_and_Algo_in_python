

def decimal_to_binary(num):
    assert num>=0 and int(num)==num,"parameter should be integer only"
    if num in [0,1]:
        return num
    else:
        # return int(str(decimal_to_binary(num//2)) + str(num%2))
        return num%2 + 10* decimal_to_binary(num//2)   
    


print(decimal_to_binary(23))
        