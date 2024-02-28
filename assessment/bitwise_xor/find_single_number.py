nums = [2,1,3,2]


def find_single_number(nums):
    n1xn2 = 0
    for num in nums :
        n1xn2^=num
    right_set_bit = 1
    while(right_set_bit&n1xn2)==0:
        right_set_bit= right_set_bit<<1
    num1 , num2 = 0, 0
    for num in nums:
        if (num & right_set_bit)!=0:
            num1^=num
        else:
            num2^=num
    return [num1,num2]

# print(find_single_number(nums))

print(2<<1)