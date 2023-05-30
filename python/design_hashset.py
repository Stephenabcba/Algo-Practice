# leetcode problem # 705. Design HashSet

"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:
0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
"""

"""
My solution: Keep a boolean array

Idea: Use a f(n) = n hash function, where the inserted key is hashed to itself
-> the key is saved in a boolean array, where True at the index means the key is in the hashset
    while False at the index means the key is not in the hashset

However, the size of the boolean array does not need to be at the full 10^6 at init()
    - the array can be expanded when larger key values are inserted

Logic:
add(): expand the array as needed, and set the index of key to True
remove(): if the key is within range of the array, set the index of key to False
contains(): if the key is within range of the array and the index of key is True, return True
    - otherwise, return False

To improve space, an improved hash function could be used where every value is mapped to a smaller range
- however, runtime would increase for every function call

Runtime:
Init: O(1)
Add: O(N) where N is the largest key into the hashset
    - however, this work is only done once in total
        - the operation could be split across multiple add() calls, as the largest key increases
Remove: O(1)
Contains: O(1)
Overall: O(M + N) where M is the number of calls to all functions and N is the largest key inserted

Space: O(N) where N is the largest key inserted into the hashset
"""

class MyHashSet:

    def __init__(self):
        self.vals = []

    def add(self, key: int) -> None:
        if key >= len(self.vals):
            self.vals += [False] * (key - len(self.vals) + 1) 
        self.vals[key] = True

    def remove(self, key: int) -> None:
        if key < len(self.vals):
            self.vals[key] = False

    def contains(self, key: int) -> bool:
        if key < len(self.vals) and self.vals[key]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)