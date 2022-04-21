// leetcode problem #705. Design HashSet

/*
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Constraints:
0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
*/

/*
My Solution:
the hashset is implemented as an array, with linear search.

when calling add(), remove(), and contains(), the methods will perform a linear search through the set and perform the necessary actions

this logic is extremely inefficient when the hashset contains many unique values.
- all operations take O(N) runtime every call, where N is the size of the hashset
*/
var MyHashSet = function () {
    this.set = []
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function (key) {
    let exists = false
    for (let item of this.set) {
        if (item == key) {
            exists = true
            break
        }
    }
    if (!exists) {
        this.set.push(key)
    }
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function (key) {
    for (let i = 0; i < this.set.length; i++) {
        if (this.set[i] == key) {
            this.set[i] = this.set[this.set.length - 1]
            this.set.pop()
            return
        }
    }
};

/** 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function (key) {
    for (let item of this.set) {
        if (item == key) {
            return true
        }
    }
    return false
};

/** 
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */

/*
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
*/

/*
Solution from leetcode discussion by Surendaar:
Constant boolean array of the input size
create an array of booleans, with index 0 corresponding to the value 0, 1 to 1, 10^6 to 10^6...

add() sets the value at index key to true
remove() sets the value at index key to false
conatains() returns the value at index key

drawback:
the program will take 10^6+1 memory as long as the instance is initialized;
- even if only 1 operation is called, 10^6+1 memory will be allocated.
*/


var MyHashSet = function () {
    this.set = []
    for (let i = 0; i <= 10 ^ 6; i++) {
        this.set.push(false)
    }
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function (key) {
    this.set[key] = true
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function (key) {
    this.set[key] = false
};

/** 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function (key) {
    return this.set[key]
};