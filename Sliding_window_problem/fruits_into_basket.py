# Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both baskets.


# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


# Time complexity -O(N) and Space Complexity-O(1)

fruits = ['A', 'B', 'C', 'B', 'B', 'C']


def fruits_int_basket(fruits):
    start =0
    max_length =0
    fruit_freq = {}
    
    for end in range(len(fruits)):
        right_fruit = fruits[end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit]=0
        fruit_freq[right_fruit]+=1
        # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
        if len(fruit_freq)>2:
            left_fruit = fruits[start]
            fruit_freq[left_fruit]-=1
            if fruit_freq[left_fruit]==0:
                del fruit_freq[left_fruit]
            start+=1
        max_length = max(max_length,end-start+1)
    return max_length


print(fruits_int_basket(fruits))
            
            
            

