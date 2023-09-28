# leetcode problem # 905. Sort Array By Parity

"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""

"""
My solution: In-place swaps with two pointers

Idea: Swap odd values in the front with even values in the back
- by doing so, all even values will be in the front and odd values in the back, satisfying problem requirements

Using 2 pointers, the program can find the first odd value from the front and the first even value from the back
- if the current value at front is even, shift the front pointer to the right until an odd value is reached
    - vice versa for the back pointer
- if the value at the front pointer is odd, the value at the back pointer is even, and front is to the left of back pointer:
    - swap values and continue

Despite having nested while loops, the inner while loops only run a total of N times
    - the iteration stops when the front pointer passes the back pointer

Runtime: O(N) where N is the length of nums list
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        front = 0
        back = len(nums) - 1
        while front < back:
            recheck = False
            while front < len(nums) and nums[front] % 2 == 0:
                front += 1
                recheck = True
            while back > 0 and nums[back] % 2 == 1:
                back -= 1
                recheck = True

            if recheck:
                continue
            
            nums[front], nums[back] = nums[back], nums[front]
        
        return nums