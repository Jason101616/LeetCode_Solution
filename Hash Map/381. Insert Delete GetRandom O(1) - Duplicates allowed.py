# Design a data structure that supports all following operations in average O(1) time.

# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
# Example:

# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();

# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);

# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);

# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);

# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();

# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);

# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();

from collections import defaultdict


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_list = []
        self.my_dict = defaultdict(lambda: set())

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        is_contain = False
        if val in self.my_dict:
            is_contain = True
        self.my_list.append(val)
        self.my_dict[val].add(len(self.my_list) - 1)
        return is_contain

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.my_dict[val]:
            return False
        for index in self.my_dict[val]:
            deleted_item_index = index
            break
        last_index = len(self.my_list) - 1
        last_item = self.my_list[last_index]

        self.my_dict[val].remove(deleted_item_index)
        if not last_index == deleted_item_index:
            self.my_list[deleted_item_index] = last_item
            self.my_dict[last_item].remove(last_index)
            self.my_dict[last_item].add(deleted_item_index)
        self.my_list = self.my_list[:-1]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        len_list = len(self.my_list)
        index = random.randint(0, len_list - 1)
        return self.my_list[index]