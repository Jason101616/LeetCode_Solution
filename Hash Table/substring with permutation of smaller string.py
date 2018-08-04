# problem in Cracking the Code interview 6th edition P70
# Given a smaller string s and a bigger string b, design an algorithm to find all permutations of the shorter string within the longer one.
# print the location of each permutation.


# idea: very like the idea as problem 30. sliding window
import collections

if __name__ == '__main__':
    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'
    s_dict = collections.defaultdict(lambda: 0)
    for char in s:
        s_dict[char] += 1
    res = []
    left = 0
    cnt = len(s_dict)
    b_dict = collections.defaultdict(lambda: 0)
    for i in range(len(b)):
        if b[i] in s_dict:
            b_dict[b[i]] += 1
            if b_dict[b[i]] == s_dict[b[i]]:
                cnt -= 1
            while b_dict[b[i]] > s_dict[b[i]]:
                b_dict[b[left]] -= 1
                if b_dict[b[left]] < s_dict[b[left]]:
                    cnt += 1
                left += 1
            if cnt == 0:
                res.append(left)
        else:
            left = i + 1
            b_dict.clear()
            cnt = len(s_dict)
    print(res)
    for i in res:
        print(b[i: i + 4])
