str1="catcatfoxfox"
words=["cat", "fox"]


def find_word_concatenation(str1, words):
    result_index = []
    # edge case
    if len(str1)==0 or len(words)==0:
        return result_index

    words_map = {}
    for word in words:
        if word not in words_map:
            words_map[word]=0
        words_map[word]+=1
    # print("words map",words_map)
    words_count = len(words)
    words_length = len(words[0])

    for i in range((len(str1)-words_count*words_length)+1):
        words_seen = {}
        for j in range(words_count):
            next_word_index = i+ j * words_length
            # get the mext word from the string
            word = str1[next_word_index:next_word_index+words_length]
            if word not in words_map:
                break


            if word not in words_seen:
                words_seen[word]=0
            words_seen[word]+=1


            if words_seen[word]>words_map.get(word,0):
                break
            if j+1 == words_count:
                result_index.append(i)

    return result_index


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()



# Time complexity
 #O(N∗M∗Len)O(N * M * Len)O(N∗M∗Len) where ‘N’ is the number of characters in the given string, ‘M’ is the total number of words, and ‘Len’ is the length of a word.


 # Space complexity - O(N+M)