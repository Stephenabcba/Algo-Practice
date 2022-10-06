# leetcode problem # 981. Time Based Key-Value Store

""""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 10^7
All the timestamps timestamp of set are strictly increasing.
At most 2 * 10^5 calls will be made to set and get.
"""

"""
My solution: Store the information as a dictionary of lists

As the problem constraints ensures that the timestamp in set() is strictly increasing, 
    it takes constant time to create a list of all key-value pairs sorted by timestamp
    -> simply append each new entry to the back of the list as the set() method is called.

From the problem definition, the get() method wants the entry with the correct key with 
    the highest timestamp smaller than the given timestamp
    -> This lends nicely to saving the data as a dictionary of lists
        - the dictionary has the key of the given key, and a value of a list
        - each item in the list holds the value and the timestamp

Example input (set() only):
set("foo","bar",1)
set("spam","eggs",2)
set("foo","bar2",3)

The resulting saved data:
{
    "foo": [(1, "bar"), (3, "bar2")],
    "spam": [(2, "eggs")]
}

Logic for each method/constructor:
Constructor:
1. Initiate the dictionary needed and save it to the object

set():
1. If needed, create a new list for the key
2. append the value and the timestamp to the end of the list corresponding to the key
- in this implementation, the data is saved in a tuple in the form (timestamp, value)
* by problem constraints, the list is always sorted based on timestamp

get():
1. retrieve the list related to the key
- There are 3 possible cases for the get() method:
    1. the list does not exist; there were no set() called with the given key
        -> return ""
    2. the list exists, but there are no entries smaller with timestamp lower than (or equal to) the given timestamp
        -> return ""
    3. the list exists, and there are at least 1 entry with timestamp lower than (or equal to) the given timestamp
        -> return the entry with the largest timestamp below the given timestamp
2. In the case where the list exists, perform a binary search to search for the highest timestamp lower than (or equal to) the given timestamp
3. Return the value if it exists, or "" if it doesn't

Runtime: O(N * log N) where N is the number of operations called
Constructor: O(1), the operation is done once, and does not depend on input size
Set(): O(1), each get() call appends to the end of a list, and could instantiate a new list
Get(): O(logM), where M is the number of entries in the list corresponding to the key
    - M ~= N in the worst case

Space: O(N), where N is the number of operations called
- each set() operation creates a new entry in the data structure
- there could be up to N set() calls
"""


class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (self.dictionary.get(key) is None):
            self.dictionary[key] = []
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        potentialValues = self.dictionary.get(key)
        if potentialValues is None:
            return ""
        start = 0
        end = len(potentialValues) - 1
        mid = (start + end) // 2
        highest = -1
        while start <= end:
            if potentialValues[mid][0] > timestamp:
                end = mid - 1
            elif potentialValues[mid][0] < timestamp:
                start = mid + 1
                highest = max(highest, mid)
            else:
                return potentialValues[mid][1]
            mid = (start + end) // 2
        if highest >= 0:
            return potentialValues[highest][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
