# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
# Time Complexity O(N)

fruits = ['A', 'B', 'C', 'B', 'B', 'C']
k=2

def fruit_into_basket(fruits,k):
    start =0
    max_length = 0
    char_frequency ={}
    
    for end in range(len(fruits)):
        right_fruit = fruits[end]
        
        if right_fruit not in char_frequency:
            char_frequency[right_fruit] =0
        char_frequency[right_fruit] +=1
        
        while len(char_frequency) >k:
            left_fruit = fruits[start]
            char_frequency[left_fruit]-=1
            if char_frequency[left_fruit]==0:
                del char_frequency[left_fruit]
            start+=1
        max_length = max(max_length,end-start+1)
    return max_length


print(fruit_into_basket(fruits,k))