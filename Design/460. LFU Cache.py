# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# idea:
# use two linked list, one for LRU, and one for LFU. it's a nested doubly linked list.
# too many edge case, keep writing if have more time.
class ListNode:
    def __init__(self, key=None, val=None):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

    def connect(self, nextNode):
        self.next = nextNode
        nextNode.prev = self


class doubly_linked_list_LRU:
    def __init__(self, freq):
        self.freq = freq
        self.sentinel_LRU = ListNode(None, None)
        self.sentinel_LRU.prev = self.sentinel_LRU
        self.sentinel_LRU.next = self.sentinel_LRU
        self.prev = None
        self.next = None

    def add(self, key, val):
        # add in the front
        new_node = ListNode(key, val)
        new_node.next = self.sentinel_LRU.next
        new_node.prev = self.sentinel_LRU
        self.sentinel_LRU.next.prev = new_node
        self.sentinel_LRU.next = new_node
        return ListNode

    def delete_node(self, node):
        # delete the node in the list
        node.prev.next = node.next
        node.next.prev = node.prev

    def delete_last(self):
        self.sentinel_LRU.prev.prev.next = self.sentinel_LRU
        self.sentinel_LRU.prev = self.sentinel_LRU.prev.prev


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.keys = {}
        self.sentinel_LFU = doubly_linked_list_LRU(None)
        self.sentinel_LFU.prev = self.sentinel_LFU
        self.sentinel_LFU.next = self.sentinel_LFU

    def get(self, key):
        pass

    def set(self, key, value):
        if key not in self.keys:
            if len(self.keys.keys()) >= capacity:
                self.sentinel_LFU.next.delete_last()
            if self.sentinel_LFU.next.freq == 1:
                node_addr = self.sentinel_LFU.next.add(key, val)
                self.keys[key] = [self.sentinel_LFU.next, node_addr]
            else:
                new_LRU_addr = doubly_linked_list_LRU(1)
                node_addr = new_LRU_addr.add(key, val)
                self.keys[key] = [new_LRU_addr, node_addr]
        else:
            LFU_addr, LRU_addr = self.keys[key]
            # ...... too many edge case, if i have time, keep writing


# another solution, written by https://discuss.leetcode.com/topic/69249/python-shitty-o-1-solution-with-two-dict-and-one-linkedlist
class ListNode(object):
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

    def connect(self, nextNode):
        self.next = nextNode
        nextNode.prev = self


class LFUCache(object):

    def __init__(self, capacity):
        """
        
        :type capacity: int
        """
        self.cap = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.connect(self.tail)
        # use to record the first ListNode of this count number
        self.cnt = {0: self.tail}
        # key: key , value:[ListNode, visit count]
        self.kv = {None: [self.tail, 0]}

    def moveforward(self, key):
        node, cnt = self.kv[key]
        self.add('tmp', node.val, cnt + 1)
        self.remove(key)
        self.kv[key] = self.kv['tmp']
        self.kv[key][0].key = key
        del self.kv['tmp']

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.kv:
            return -1
        self.moveforward(key)
        return self.kv[key][0].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            return
        if key in self.kv:
            self.kv[key][0].val = value
            self.moveforward(key)
            return
        if len(self.kv) > self.cap:
            self.remove(self.tail.prev.key)
        self.add(key, value, 0)

    def remove(self, key):
        node, cnt = self.kv[key]
        if self.cnt[cnt] != node:
            node.prev.connect(node.next)
        elif self.kv[node.next.key][1] == cnt:
            node.prev.connect(node.next)
            self.cnt[cnt] = self.cnt[cnt].next
        else:
            node.prev.connect(node.next)
            del self.cnt[cnt]
        del self.kv[key]

    def add(self, key, value, cnt):
        if cnt in self.cnt:
            loc = self.cnt[cnt]
        else:
            loc = self.cnt[cnt - 1]
        node = ListNode(key, value)
        loc.prev.connect(node)
        node.connect(loc)
        self.cnt[cnt] = node
        self.kv[key] = [node, cnt]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
