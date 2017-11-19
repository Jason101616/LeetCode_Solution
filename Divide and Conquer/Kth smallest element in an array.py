import queue


# Solution 1: use divide and conquer
def paritition(nums):
    pivot_val = nums[0]
    pivot_pos = 0
    len_nums = len(nums)
    for i in range(1, len_nums):
        if nums[i] < pivot_val:
            pivot_pos += 1
            if i != pivot_pos:
                nums[i], nums[pivot_pos] = nums[pivot_pos], nums[i]
    nums[0] = nums[pivot_pos]
    nums[pivot_pos] = pivot_val
    return pivot_pos


def find_k_small(nums, k):
    pivot_pos = paritition(nums)
    if pivot_pos == k - 1:
        return nums[pivot_pos]
    elif pivot_pos > k - 1:
        return find_k_small(nums[:pivot_pos], k)
    else:
        return find_k_small(nums[pivot_pos + 1:], k - pivot_pos - 1)


# Solution 2: use heap
def find_k_small_heap(nums, k):
    pri_queue = queue.PriorityQueue()
    for num in nums:
        pri_queue.put(-num)
        if pri_queue.qsize() > k:
            pri_queue.get()
    return -pri_queue.get()


if __name__ == '__main__':
    nums = [3, 1, 2, 4, 6]
    ans = find_k_small(nums, 1)
    print(ans)
