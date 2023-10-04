# leetcode problem # 706. Design HashMap

"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:
0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
"""

"""
My solution: Custom hash function

Hash function logic: The hashed key is simply the key modulo the size of the hashmap
- the size of the hashmap is made to be a prime number to minimize collisions
- in the case of collisions, each slot in the hashmap is a list
    - every key-value pair with the same hashed key is placed into the same list

Logic for each method:
1. init: create a list of lists
2. put:
    i. find the hashed key
    ii. find whether the key has been entered before
    iii. if the key has been entered before, update the value attached to the key
    iv. otherwise, add a new key-value pair as a list into the corresponding list
3. get:
    i. find the hashed key
    ii. find whether the key is in the hashmap
    iii. return the associated value, or -1 if not found
4. delete:
    i. find the hashed key
    ii. find whether the key is in the hashmap
    iii. remove the key-value pair from the list

Runtime: O(N^2) where N is the number of calls made
- in the worst case, the values are hashed to the same value over and over
    - collission makes this hash function slow down
- in the average case, the values are spread out and do not collide
    - the average case should be closer to Theta(N)
Space: O(N)
"""


class MyHashMap:

    def __init__(self):
        self.hashVal = 1009
        self.hashMap = [[] for _ in range(self.hashVal)]
        

    def put(self, key: int, value: int) -> None:
        hashedKey = key % self.hashVal
        newPair = True
        for pair in self.hashMap[hashedKey]:
            if pair[0] == key:
                pair[1] = value
                newPair = False
                break
        if newPair:
            self.hashMap[hashedKey].append([key, value])

    def get(self, key: int) -> int:
        hashedKey = key % self.hashVal
        for pair in self.hashMap[hashedKey]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        hashedKey = key % self.hashVal

        for idx, pair in enumerate(self.hashMap[hashedKey]):
            if pair[0] == key:
                self.hashMap[hashedKey] = self.hashMap[hashedKey][:idx] + self.hashMap[hashedKey][idx + 1:]
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)