import math
input = [1,5,12,2,11,5]
k = 3

# brute force approach
def find_kth_smallest_number(input, k):
    prev_smallest, prev_smallest_index = -math.inf , -1
    curr_smallest, curr_smallest_index = math.inf , -1

    for i in range(k):
        for j in range(len(input)):
            if input[j]>prev_smallest and input[j]<curr_smallest:
                curr_smallest = input[j]
                curr_smallest_index = j
            elif input[j]==prev_smallest and j>prev_smallest_index:
                curr_smallest = input[j]
                curr_smallest_index = j 
                break
        prev_smallest = curr_smallest
        prev_smallest_index = curr_smallest_index
        curr_smallest = math.inf
    return prev_smallest


print(find_kth_smallest_number(input, k))

# time complexity: O(k*n)
# space complexity: O(1)

# using max heap

from heapq import *

# def find_kth_smallest_number(input, k):
#     max_heap = []
#     for i in range(k):
#         heappush(max_heap, -input[i])
#     for i in range(k, len(input)):
#         if -input[i]>max_heap[0]:
#             heappop(max_heap)
#             heappush(max_heap, -input[i])
#     return -max_heap[0]

# print(find_kth_smallest_number(input, k))

# time complexity: O(k+(n-k)*logk)
# space complexity: O(k)

# using min heap

def find_kth_smallest_number(input, k):
    min_heap = []
    for i in range(len(input)):
        heappush(min_heap, input[i])
    for i in range(k):
        heappop(min_heap)
    return min_heap[0]

print(find_kth_smallest_number(input, k))

# time complexity: O(n+(n-k)*logn)
# space complexity: O(n)

# using quick select
def find_kth_smallest_number(input, k):
    return quick_select(input, k, 0, len(input)-1)
def quick_select(input, k, start, end):
    pivot = partition(input, start, end)
    if pivot==k-1:
        return input[pivot]
    if pivot>k-1:
        return quick_select(input, k, start, pivot-1)
    else:
        return quick_select(input, k, pivot+1, end)
def partition(input, start, end):
    pivot = end
    for i in range(start, end):
        if input[i]>input[pivot]:
            input[i], input[pivot] = input[pivot], input[i]
    input[pivot], input[i] = input[i], input[pivot]
    return pivot


