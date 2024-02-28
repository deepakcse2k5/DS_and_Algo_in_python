from heapq import *
str = "Programming"

def sort_character_by_frequency(str):
    char_freq_map = {}
    for char in str:
        char_freq_map[char] = char_freq_map.get(char,0) +1

    max_heap = []

    for char, freq in char_freq_map.items():
        heappush(max_heap,(-freq,char))

    sortedString = []

    while max_heap:
        freq, char = heappop(max_heap)
        for _ in range(-freq):
            sortedString.append(char)
    return ''.join(sortedString)

print(sort_character_by_frequency(str))

# Time Complexity - O(D*logD) where D is the distinct character of a string.In worst case, it is O(N*logN) , where N is the number of string

# Space Complexity :- O(N)

