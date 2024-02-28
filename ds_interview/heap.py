import heapq

nums = [13,5,2,6,10,9,7,4,3]
k=5

heapq.heapify(nums)

find_largest =heapq.nlargest(k,nums).pop()

find_smallest = heapq.nsmallest(k,nums).pop()
print(find_largest)
print(find_smallest)