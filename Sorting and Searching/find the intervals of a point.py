# 给一堆区间，比如 [-1.1, 1.0], [-0.5, 3.5], [3.6, 4.0], ...，再给一个点target，比如0.1，要返回所有包含了这个点的区间。
# 最简单的做法就是一个一个区间比较，返回所有包含了target的区间，这是linear time
# 又问，可以对这些区间做pre-processing，pre-processing只做一次所以复杂度不计。问怎么做可以比linear time更快。
# 和面试官讨论的大致思路是，按照区间左端点做sorting，然后binary search。

# idea: 把所有区间的起点和终点放一起排序，然后遍历，遇到起点加区间，遇到终点减区间，这样就可以得到所有小区间覆盖的区间。
# 查询的时候用binary search

import copy
from collections import defaultdict


def find_interval(intervals, point):
    critical_point = []
    for interval in intervals:
        critical_point.append(interval[0])
        critical_point.append(interval[1])

    critical_point = sorted(list(set(critical_point)))
    critical_dict = defaultdict(lambda: [])
    for i in range(len(critical_point)):
        if i > 0:
            critical_dict[critical_point[i]] = copy.deepcopy(critical_dict[critical_point[i - 1]])
        for interval in intervals:
            if interval[0] == critical_point[i]:
                critical_dict[critical_point[i]].append(interval)
            if interval[1] == critical_point[i]:
                critical_dict[critical_point[i]].remove(interval)
    left, right = 0, len(critical_point) - 1
    while left < right:
        mid = (left + right) // 2
        if critical_point[mid] <= point:
            left = mid + 1
        else:
            right = mid
    if critical_point[left] > point:
        left -= 1
    return critical_dict[critical_point[left]]


if __name__ == '__main__':
    intervals = [[-1.1, 1.0], [-0.5, 3.5], [3.6, 4.0]]
    val = -0.1
    ans = find_interval(intervals, val)
    print(ans)
