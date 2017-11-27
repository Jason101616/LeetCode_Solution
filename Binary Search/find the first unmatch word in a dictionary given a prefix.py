# 给定一个单词前缀和一个字典序排序的字典， 找到第一个前缀不符合条件的单词


def is_prefix(word1, word2):
    return word1[:len(word2)] == word2


# idea: use binary search
def prefixDict(worddict, prefix):
    left, right = 0, len(worddict) - 1
    while left < right:
        mid = (left + right) // 2
        if is_prefix(worddict[mid], prefix):
            left = mid + 1
        else:
            right = mid
    if is_prefix(worddict[left], prefix):
        return -1
    return worddict[left]


if __name__ == '__main__':
    worddict = ["ab", "abc", "abb", "abc", "acx"]
    prefix = 'ab'
    ans = prefixDict(worddict, prefix)
    print(ans)