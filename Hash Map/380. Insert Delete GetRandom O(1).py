# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
# Example:

# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

# idea: use list to store the val, use dictionary to store the index of the val
from random import randint


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_dict = {}
        self.my_list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.my_dict:
            return False
        self.my_list.append(val)
        self.my_dict[val] = len(self.my_list) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # idea is swap this item with the last item in my_list
        if val not in self.my_dict:
            return False
        remove_item_index = self.my_dict[val]
        last_item_index = len(self.my_list) - 1
        last_item = self.my_list[last_item_index]
        del self.my_dict[val]
        # if the removed item is the last item, we don't need to re-insert it
        if remove_item_index != last_item_index:
            self.my_list[remove_item_index] = last_item
            self.my_dict[last_item] = remove_item_index
        self.my_list.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        len_list = len(self.my_list)
        index = randint(0, len_list - 1)
        return self.my_list[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()