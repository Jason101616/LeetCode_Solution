/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 // capacity // );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
*/

/*idea: 
(1) maintain a cache_list which contains cache_node.
(2) use an unordered_map(key, the address of the key in the list) cache_list to facilitate the quick finding.
pseudocode: 
def get(key):
	if find the key:
		duplicate the node and put it to the front of the list
		delete the node in the previous position
		update cache_map
		return key->value
	else:
		return -1

def put(key, value):
	if the key is in the cache_map:
		key->value = value
		duplicate the node and put it to the front of the list
		delete the node in the previous position
		update cache_map
	else
		if cache_list.size() == capacity:
			in cache_map: remove the key-address pair of the last element in the cache_list
			remove the last element in the cache_list

		construct a new cache_node(key, value) and push it in the front of the cache_list
		update cache_map
*/

class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (cache_map.find(key) != cache_map.end()) {
            cache_list.push_front(*cache_map[key]);
            cache_list.erase(cache_map[key]);
            cache_map[key] = cache_list.begin();
            return cache_list.front().value;
        }
        else
            return -1;
    }
    
    void put(int key, int value) {
        if (cache_map.find(key) != cache_map.end()) {
            (*cache_map[key]).value = value;
            cache_list.push_front(*cache_map[key]);
            cache_list.erase(cache_map[key]);
            cache_map[key] = cache_list.begin();
        }
        else {
            if (cache_list.size() == capacity) {
                cache_map.erase(cache_list.back().key);
                cache_list.pop_back();
            }
            cache_list.push_front(cache_node(key, value));
            cache_map[key] = cache_list.begin();
        }
    }
private:
    struct cache_node {
        int key, value;
        cache_node (int k, int v): key(k), value(v) {}
    };
    int capacity;
    unordered_map<int, list<cache_node>::iterator> cache_map;// store (key, address in list)
    list<cache_node> cache_list;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
