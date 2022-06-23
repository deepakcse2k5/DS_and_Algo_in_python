# input = [1,3,5]
# output = [[],[1],[3],[5],[1,3],[1,5],[3,5],[1,3,5]]


def find_subsets(nums):
    subset = []
    subset.append([])
    for curr_num in nums:
        n = len(subset)
        for i in range(n):
            set1 = list(subset[i])
            set1.append(curr_num)
            subset.append(set1)
    return subset


def main():
    print("list of subsets: " + str(find_subsets([1, 3])))
    print("list of subset: " + str(find_subsets([1, 4, 6])))

main()

# Time complexity#
#
# Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of O(2N)O(2^N)O(2​N​​) subsets, where ‘N’ is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be O(N∗2N)O(N*2^N)O(N∗2​N​​).
# Space complexity#
#
# All the additional space used by our algorithm is for the output list. Since we will have a total of O(2N)O(2^N)O(2​N​​) subsets, and each subset can take up to O(N)O(N)O(N) space, therefore, the space complexity of our algorithm will be O(N∗2N)O(N*2^N)O(N∗2​N​​).

