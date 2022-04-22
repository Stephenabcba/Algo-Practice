// leetcode problem #706. Design HashMap

/*
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Constraints:
0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
*/

/*
My Solution: simple hashing function with array of arrays (of arrays)
Hashing function:
    the hashed key is key % 1000
    - the values within the range are basically evenly distributed to each hashed key
The data structure has an outer array of size 1000, corresponding to each hashed key value
Each item in the array are also arrays, to hold duplicate values that are hashed to the same spot

when calling any of the operations, hash the key first.
    the only search area is the outer array at index of hashed key
when calling put():
    search inside the map[hashedKey] for the key
    if key exists: change the value to the new value
    if key doesn't exist: add the key-value pair to the array as [key,value]
when calling get():
    search inside the map[hashedKey] for the key
    if key exists: return the value
    if key doesn't exist: return -1
when calling remove():
    search inside the map[hashedKey] for the key
    if key exists: copy the last item of the map[hashedKey] array to the current index, and pop from the array
    if key doesn't exist: do nothing

Runtime: O(N) where the worst case is all the values are hashed to the same index
    - however, on the average case, the added values will be evenly distributed throughout each index
        - this should significantly reduce the time to search for an item when the hashmap is large.
Space: O(N), where N is the number of put() calls with unique keys
*/
var MyHashMap = function () {
    this.map = []
    for (let i = 0; i < 1000; i++) {
        this.map.push([])
    }
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function (key, value) {
    let hashedKey = key % 1000
    for (let item of this.map[hashedKey]) {
        if (item[0] == key) {
            item[1] = value
            return
        }
    }
    this.map[hashedKey].push([key, value])

};

/** 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function (key) {
    let hashedKey = key % 1000
    for (let item of this.map[hashedKey]) {
        if (item[0] == key) {
            return item[1]
        }
    }
    return -1
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function (key) {
    let hashedKey = key % 1000
    for (let i = 0; i < this.map[hashedKey].length; i++) {
        if (this.map[hashedKey][i][0] == key) {
            this.map[hashedKey][i] = this.map[hashedKey][this.map[hashedKey].length - 1]
            this.map[hashedKey].pop()
            break
        }
    }
};

/** 
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */

/*
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
*/