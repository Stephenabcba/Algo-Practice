# leetcode problem # 219. Contains Duplicate II

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""

"""
My solution: Use dictionaries to track index of each value

Pseudo-Code:
1. for each unique value, keep track of all indeces where the value exists in the list
2. for each unique value, check if any difference in indeces is below threshold K
- If there is, return True
- Observation: the smallest difference in index would never skip between values
    - ex: if the number 1 occurs at indeces 0, 4, 5, the smallest difference would never be 0 and 5 (5 - 0 = 5)
        - instead, the smallest difference is between 4 and 5 (5 - 4 = 1)
3. If none of the values have difference below threshold, return False

Runtime: O(N), where N is the number of values in List nums
- Even though there is a nested for-loop in the logic, the loops only run N times in total.
Space: O(N), where N is the number of values in List nums
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        for idx, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(idx)

        for values in positions.values():
            for idx in range(len(values) - 1):
                if values[idx + 1] - values[idx] <= k:
                    return True

        return False


"""
Solution from leetcode discussion by ayushsenapati123 (originally written in C++)

Builds upon observation in pseudo code step 2 above:
- If step 2 above is done as step 1 is processing, the dictionary does not need to hold multiple indeces for a given value with duplicates.
    - if previous index and current index does not meet requirement, there's no reason to keep track of previous index
        - ex: num == 1, k == 2, previous index == 0, current index == 4:
            - 4 - 0 = 4 > 2; previous index of 0 does not provide any more information if the number 1 is found in more indeces later.

Runtime and Space remains O(N), but saves on space and can be done in 1 pass instead of 2.
"""


class SolutionImproved:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        for idx, num in enumerate(nums):
            if num in positions and idx - positions[num] <= k:
                return True
            positions[num] = idx

        return False
