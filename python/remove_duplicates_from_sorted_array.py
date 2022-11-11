# leetcode problem # 26. Remove Duplicates from Sorted Array

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

"""
My solution: Two-pointers approach

As the array is sorted, all duplicated values are grouped together
- ex: if there are five "2"s in the array, they must appear as [2, 2, 2, 2, 2] with nothing in between

One pointer keeps track of which value is currently being processed
- In the solution, it is the iterating variable idx in the for loop
The other pointer keeps track of the first available space to copy a valid value into
- In the solution, it is the variable curIdx

Logic:
Iterate through every value in the array
    - If the numerical value has been processed before, move on to the next value
    - If the numerical value has not been processed before, copy the value to the first available space
        * as the array is sorted, the algorithm only needs to keep track of the last value processed.

Runtime: O(N) where N is the number of values in list nums
Space: O(1), the algorithm does not use any extra space that scales with input
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # returnIdx = 1
        curIdx = 1
        prevNum = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] != prevNum:
                nums[curIdx] = nums[idx]
                prevNum = nums[idx]
                curIdx += 1
            # returnIdx += 1

        return curIdx
