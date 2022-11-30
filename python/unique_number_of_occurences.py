# leetcode problem # 1207. Unique Number of Occurrences

"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

"""
My solution: Use a dictionary and a set

Logic:
1. Get the count of every value using a dictionary, where key is the number and value is the count of occurrences of the number
2. Use a set to keep track of the occurrences seen after every number has been processed
- if a specific occurrence has been seen again, return False
3. If all occurrences are unique (didn't return False in step 2), return True

Runtime: O(N) where N is the number of values in list arr
Space: O(N) where N is the number of values in list arr
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numCounts = {}
        for num in arr:
            numCounts[num] = numCounts.get(num, 0) + 1

        occurrenceSet = set()

        for occurrence in numCounts.values():
            if occurrence in occurrenceSet:
                return False
            occurrenceSet.add(occurrence)

        return True
