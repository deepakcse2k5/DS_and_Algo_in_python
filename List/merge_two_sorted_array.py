# input
lst1 = [1, 3, 4, 5]
lst2 = [2, 6, 7, 8]


# Time complexity - O(mn) , where n is the length of list1 and m is the length of list2
# space complexity - O(m)

def merge_two_sorted_array(lst1, lst2):
    ind1, ind2 = 0, 0

    while ind1 < len(lst1) and ind2 < len(lst2):
        if lst1[ind1] > lst2[ind2]:
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1
    if ind2 < len(lst2):
        lst1.extend(lst2[ind2:])
    return lst1


def main():
    print(merge_two_sorted_array(lst1, lst2))


main()
