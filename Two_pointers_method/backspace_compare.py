# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
# Time complexity is O(M+N) where M and N is the length of input string
# Space Complexity O(1)

from collections import Counter
str1="xywrrmp"
str2="xywrrmu#p"



def backspace_compare(str1,str2):
    index1 = len(str1)-1
    index2 = len(str2)-1
    
    while(index1>=0 and index2>=0):
        i1 = next_valid_char_index(str1,index1)
        i2 = next_valid_char_index(str2,index2)
        if index1<0 and index2<0:
            return True
        if index1 <0 or index2<0:
            return False
        if str1[i1]!=str2[i2]:
            False
        index1 = i1-1
        index2 = i2-1
    return True

def next_valid_char_index(str,index):
    backspace_count =0
    while(index>0):
        if str[index]=='#':
            backspace_count+=1
        elif backspace_count>0:
            backspace_count-=1
        else:
            break
        index-=1
    return index


print(backspace_compare(str1,str2))



            