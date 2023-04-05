# leetcode problem # 2439. Minimize Maximum of Array

"""
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.

Example 1:
Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.

Example 2:
Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

Constraints:

n == nums.length
2 <= n <= 10^5
0 <= nums[i] <= 10^9
"""

"""
My solution: binary search

Intuition:
Make a guess on the minimum mazimum value, and check.
The minimum value of the guess is the first value in nums, as that value will never decrease
The maximum value of the guess is the largest value in nums, as there's no point increasing that value
Using binary seach, the program will make the fewest guesses before getting to the answer

Checking logic:
for each guess, calculate a diff equal to the sum of every value - mid
    - if the diff is greater than 0 at any time, the guess is invalid
        - when this happens, there's a value remaining in nums that's larger than the guess
if the diff is less than or equal to 0, the real value is smaller than or equal to the guess
otherwise, the real value is larger than the guess


Runtime: O(N * logM) where N is the length of nums list, and M is the largest value in nums
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        small = nums[0]
        large = max(nums)

        while small < large:
            mid = (small + large) // 2
            diff = 0
            for num in nums:
                diff += num - mid
                if diff > 0:
                    break
            if diff <= 0:
                large = mid
            else:
                small = mid + 1

        return small


"""
Solution by leetcode: prefix sum

Iterate over each value, and calculate the prefix sum along the way
- Try to distribute the prefix sum over the current pool of values
    - divide the prefix sum by the number of values and round up
    -> this "flattens" the peaks to minimize the maximum value
- the largest of the distributed prefix sum is the answer
    - as it's impossible to "move" the values to the right, the highest 
    "flattened" peak will stay in place

Runtime: O(N) where N is the length of nums list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # Initialize answer and the prefix sum.
        answer = 0
        prefix_sum = 0

        # Iterate over nums, update prefix sum and answer.
        for i in range(len(nums)):
            prefix_sum += nums[i]
            answer = max(answer, math.ceil(prefix_sum / (i + 1)))

        return answer
