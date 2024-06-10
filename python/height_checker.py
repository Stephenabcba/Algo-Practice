# leetcode problem # 1051. Height Checker

"""
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Example 2:
Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

Example 3:
Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100
"""

"""
My solution: Sort then solve (using default sorting)

After sorting, count the number of differences

Runtime: O(N * logN), where N is the length of heights list
Space: O(N)
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)

        differences = 0

        for idx in range(len(heights)):
            if heights[idx] != sortedHeights[idx]:
                differences += 1

        return differences


"""
Solution by leetcode: Counting Sort

Instead of using the default sort method, the counting sort method is implemented manually and used

Advantage of counting sort: Faster than N*logN, especially when the range of the list to be sorted is small
- the logic is also fairly straightforward, making it easy to implement

* interesting note: counting sort is not a comparison sort

Runtime: O(n + k), where n is the length of heights, and k is the range of heights
Space: O(n)
"""


class Solution:
    def counting_sort(self, arr):
        # Create the counting hash map.
        counts = {}
        # Find the minimum and maximum values in the array.
        min_val, max_val = min(arr), max(arr)

        # Update element's count in the hash map.
        for val in arr:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

        index = 0
        # Place each element in its correct position in the array.
        for val in range(min_val, max_val + 1):
            # Append all 'val's together if they exist.
            while counts.get(val, 0) > 0:
                arr[index] = val
                index += 1
                counts[val] -= 1

    def heightChecker(self, heights: List[int]) -> int:
        # Sort the array using counting sort.
        sorted_heights = heights[:]
        self.counting_sort(sorted_heights)

        count = 0
        # Loop through the original and sorted arrays.
        for i in range(len(sorted_heights)):
            # Increment count if elements at the same index differ.
            if heights[i] != sorted_heights[i]:
                count += 1
        # Return the total count of differing elements.
        return count
