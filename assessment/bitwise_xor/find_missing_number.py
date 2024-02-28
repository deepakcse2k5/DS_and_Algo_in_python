nums = [1,5,2,6,4]

# def find_missing_number(nums):
#     if len(nums)==0:
#         return
#     n = len(nums)+1
#     s1 = 0
#     for i in range(1,n+1):
#         s1+=1
#     for i in s1:
#         s1-=1
#     return s1

# print(find_missing_number(nums))


def find_missing_num(nums):
    x1 = [i for i in range(nums)]

print(find_missing_num(nums))