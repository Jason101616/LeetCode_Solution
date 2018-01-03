// Design and implement a TwoSum class. It should support the following
// operations: add and find.

// add - Add the number to an internal data structure.
// find - Find if there exists any pair of numbers which sum is equal to the
// value.

// For example,
// add(1); add(3); add(5);
// find(4) -> true
// find(7) -> false

#include <unordered_map>
using namespace std;
class TwoSum {
  public:
    /** Initialize your data structure here. */

    /** Add the number to an internal data structure.. */
    void add(int number) {
        if (test.find(number) == test.end()) {
            test[number] = 1;
        } else {
            test[number] += 1;
        }
    }

    /** Find if there exists any pair of numbers which sum is equal to the
     * value. */
    bool find(int value) {
        for (auto it = test.begin(); it != test.end(); it++) {
            int i = it->first;
            int j = value - i;
            if (i == j && it->second > 1 ||
                i != j && test.find(j) != test.end()) {
                return true;
            }
        }
        return false;
    }

  private:
    unordered_map<int, int> test;
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * bool param_2 = obj.find(value);
 */