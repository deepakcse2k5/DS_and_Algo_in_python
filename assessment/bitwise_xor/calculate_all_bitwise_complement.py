def calculate_all_bitwise_complement(num):
    if num==0:
        return 1
    bit_count, n = 0 , num
    while n >0:
        bit_count+=1
        n= n >>1
    
    all_bit_set = pow(2,bit_count)-1

    return num ^ all_bit_set


print(calculate_all_bitwise_complement(8))
print(calculate_all_bitwise_complement(10))