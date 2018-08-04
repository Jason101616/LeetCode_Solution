# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dummy = ListNode(None, None)  # the node in the front is the most recently used data
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.mapping = {}  # key is the key, value is the address of the ListNode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mapping:
            self.move_front(key)
            return self.mapping[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.mapping:
            # update the node and move it to the front
            self.mapping[key].val = value
            self.move_front(key)
        else:
            self.size += 1
            # need evict now
            if self.size > self.capacity:
                # evict the LRU data
                del self.mapping[self.dummy.prev.key]
                self.delete_back()
                self.size -= 1
            # generate a new node and put it in the front of the doubly linked list  
            new_node = ListNode(key, value)
            self.mapping[key] = new_node
            self.insert_front(key)

    def move_front(self, key):
        # move the node forward
        node = self.mapping[key]
        front_n = node.prev
        next_n = node.next
        front_n.next = next_n
        next_n.prev = front_n
        self.insert_front(key)

    def insert_front(self, key):
        # insert the node front
        node = self.mapping[key]
        next_n = self.dummy.next
        self.dummy.next = node
        node.next = next_n
        next_n.prev = node
        node.prev = self.dummy

    def delete_back(self):
        # delete the last node
        prev_prev = self.dummy.prev.prev
        prev_prev.next = self.dummy
        self.dummy.prev = prev_prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
