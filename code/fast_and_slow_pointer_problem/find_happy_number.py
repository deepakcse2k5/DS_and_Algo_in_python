# To find happy number

# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:
# 1. 2​^2​​+3^​2​​ = 4 + 9 = 13
# 2. 1^2+3^2  = 1 + 9 = 10
# 3. 1^2 + 0^2 = 1 + 0 = 1
# Time complexity - O(N) and space complexity - O(1)


def find_happy_number(num):
    slow, fast = num,num
    while True:
        slow = find_square_number(slow)
        fast = find_square_number(find_square_number(fast))
        if slow==fast:
            break
    return slow==1
        
        
def find_square_number(num):
    sum =0
    while(num>0):
        digit = num %10
        sum += digit*digit
        num //=10
    return sum
        
        
        
print(find_happy_number(23))

print(find_happy_number(12))