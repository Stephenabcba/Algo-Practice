# leetcode problem # 380. Insert Delete GetRandom O(1)

"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

"""
My solution: Use a set and convert to array when needed

When inserting and removing, use standard set operations and return result as specified

When calling getRandom(), convert the set to a list and use random() to get a random index to return

Runtime:
Insert: O(1)
Remove: O(1)
getRandom: O(N)
Space: O(N) for number of insert operations called
"""




import random
import math
class RandomizedSet:

    def __init__(self):
        self.valueSet = set()

    def insert(self, val: int) -> bool:
        if val in self.valueSet:
            return False
        self.valueSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueSet:
            return False

        self.valueSet.remove(val)

        return True

    def getRandom(self) -> int:
        tempList = list(self.valueSet)
        return tempList[math.floor(random.random() * len(tempList))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


"""
My original attempt, modified using information from Solution by md2030

Use a dictionary and a list to keep track of the data
The dictionary has the inserted value as key, and the index in the list as value
The list holds all inserted values that have not been removed (no duplicates)

Insert Operation:
If the value already existed (found in dictionary), return False
Otherwise:
    Add value to the dictionary (with correct index)
    Add value to the list
    Return True

Remove Operation:
If the value didn't exist (not in dictionary), return False
Otherwise:
    "Swap" the value in the last index of the list with the removed value
        1. in the dictionary: update the dictionary index for the value in the last index
        2. in the list: change the removed value's index's value to the value in the last index
            - effectively swapping the removed value with the last value in the list
                - as the removed value will be popped anyways, only the half of the swap is done
        3. in the list: pop from the list
        4. in the dictionary: delete the entry for the removed value
** My attempts failed test cases because I forgot to perform step 1.

getRandom Operation:
Using the random.random() and math.floor() methods, a random value can be extracted from the list
- Using random.random(), get a random decimal value between 0 and 1
- Multiply the random value by the length of the list, then truncate it using math.floor()
- The resulting value is a randomized index within the bounds of the list
- return the value at the random index of the list


Runtime:
Insert: O(1)
Remove: O(1)
getRandom: O(1)
Space: O(N) for number of insert operations called
"""

# import random
# import math


class RandomizedSet2:

    def __init__(self):
        self.valueDict = {}
        self.valueList = []

    def insert(self, val: int) -> bool:
        if val in self.valueDict:
            return False
        self.valueDict[val] = len(self.valueList)
        self.valueList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueDict:
            return False

        self.valueDict[self.valueList[-1]] = self.valueDict[val]
        self.valueList[self.valueDict[val]] = self.valueList[-1]
        self.valueList.pop()
        del self.valueDict[val]
        return True

    def getRandom(self) -> int:
        return self.valueList[math.floor(random.random() * len(self.valueList))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
