# leetcode problem # 146. LRU Cache

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

"""
My solution: dictionary with heap

Idea:
1. A dictionary is used to quickly retrieve the values of the key.
    - the key is the key in the cache, and the value of the dictionary is an array
        - the array contains the key, the value of the cache, and the step value (detailed below)
2. A heap is used to quickly find the LRU entry to delete.
    - the program can find the smallest entry in O(1) time
        - updating the heap takes O(logM) time, where M is the size of the cache
3. To make use of the heap, a step value is attached to the entries
    - the step value is incremented every time an entry is added or modified
    - the step value of the entry is updated when the enry is accessed
    -> when an entry needs to be deleted, delete the smallest entry in the cache

Runtime: O(N * M) overall where N is the number of calls and M is the capacity of the cache
    - it takes O(1) time to initialize the cache
    - it takes O(1) time to get any value in the cache
    - it takes O(M) time to put a value into the cache
        - if the cache is not full, it takes O(1) time to put values into the cache
Space: O(M)
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.step = 0
        self.cacheLen = 0
        self.cacheDict = {}
        self.lruOrder = []

    def get(self, key: int) -> int:
        if key in self.cacheDict:
            self.cacheDict[key][0] = self.step
            self.step += 1
        return self.cacheDict.get(key, [-1, -1])[1]

    def put(self, key: int, value: int) -> None:
        if key in self.cacheDict:
            self.cacheDict[key][0] = self.step
            self.step += 1
            self.cacheDict[key][1] = value
        else:
            if self.cacheLen == self.capacity:
                heapq.heapify(self.lruOrder)
                self.cacheLen -= 1
                oldStep, oldVal, oldKey = heapq.heappop(self.lruOrder)
                del self.cacheDict[oldKey]
            self.cacheLen += 1
            self.cacheDict[key] = [self.step, value, key]
            self.lruOrder.append(self.cacheDict[key])
            self.step += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
Improvement: Using DLL instead of heap

From the related topics in leetcode, Doubly-Linked list is a concept that could be applied to 
improve runtime.

Instead of using the heap, a doubly-linked list is used to manage the order to delete from the cache
when it is full.

A dictionary is still used to quickly access the values for each key in the cache
- the key is the key of the cache, and the value is a node in the DLL

DLL management:
1. When a key is accessed through get() or the value of an existing key is updated through put(),
    move the corressponding node to the end of the DLL
    - the node can be accessed through the dictionary with the key
2. When the cache is full, delete the first node in the DLL
    - update the head and tail accordingly when needed
    - delete the corresponding key in the dictionary

Runtime: O(N) overall where N is the number of calls
    - it takes O(1) time to initialize the cache
    - it takes O(1) time to get any value in the cache
    - it takes O(1) time to put a value into the cache
Space: O(M) where M is the capacity of the cache
"""

class LRUNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheLen = 0
        self.cacheDict = {}
        self.lruTail = None
        self.lruHead = None

    def get(self, key: int) -> int:
        if key in self.cacheDict:
            self.reconnect(self.cacheDict[key])
            return self.cacheDict[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheDict:
            self.cacheDict[key].value = value
            self.reconnect(self.cacheDict[key])
        else:
            if self.cacheLen == self.capacity:
                oldHead = self.lruHead
                self.lruHead = self.lruHead.next
                oldHead.next = None
                if self.lruHead:
                    self.lruHead.prev = None
                else:
                    self.lruTail = None
                self.cacheLen -= 1
                del self.cacheDict[oldHead.key]
            self.cacheLen += 1
            self.cacheDict[key] = LRUNode(key, value)
            if self.lruHead is None:
                self.lruHead = self.cacheDict[key]
                self.lruTail = self.cacheDict[key]
            else:
                self.lruTail.next = self.cacheDict[key]
                self.cacheDict[key].prev = self.lruTail
                self.lruTail = self.cacheDict[key]

    def reconnect(self, node) -> None:
        if self.cacheLen > 1 and node is not self.lruTail:
            if node is self.lruHead:
                self.lruHead = node.next
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = None
            node.next = None
            self.lruTail.next = node
            node.prev = self.lruTail
            self.lruTail = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)