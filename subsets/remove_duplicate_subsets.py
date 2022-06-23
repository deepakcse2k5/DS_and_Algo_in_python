def remove_duplicate_subsets(nums):
    subsets = []
    subsets.append([])
    for curr_num in nums:
        n = len(subsets)
        print(n)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(curr_num)
            print(set1)
            if set1 not in subsets:
                subsets.append(set1)
            print("******")
    return subsets


def main():
    print("list of subsets: " + str(remove_duplicate_subsets([1, 3, 3])))

main()



