// leetcode problem #581. Shortest Unsorted Continuous Subarray

/*
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

(not mentioned in examples or problem statement: duplicate numbers are allowed in test cases)

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
*/

/*
My solution: Greedy search for end of unsorted array
- Idea (if no duplicate values)
    - The unsorted array ends at the last index i where nums[i] < nums[i-1] ("conflict")
        - keep track of a variable of the last "conflict" index
            - loop through the array to find the last conflict
    - The unsorted array starts at the first index j where nums[j] is larger than the minimum value found inside the unsorted array
        - this is done in a second loop
        - the minimum value within the unsorted array can be found in the first loop
    - The length is (end index - start index + 1)
- Adaptation for duplicate values:
    - keep track of the max value of the unsorted array, in addition to the min value
        - in the way the solution is set up, check the value of the previous index for the max value
    - include all values between the range [min,max)
        - do not need to retroactively include previous indexes

Runtime: O(N), there are 2 loops in parallel with each other
Space: O(1), the solution space requirement does not scale with input size at all
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function (nums) {
    let last = -1 // where the unsorted array ends
    let min = Infinity // used for searching for start of the array
    let max = -Infinity // used for duplicate values

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1] || (nums[i] >= min && nums[i] < max)) {
            last = i
            if (nums[i] < min) {
                min = nums[i]
            }
            if (nums[i - 1] > max) {
                max = nums[i - 1]
            }
        }
    }

    if (last < 0) { // the array is completely sorted (no unsorted array)
        return 0
    }

    // look for the start of the unsorted array
    for (let i = 0; i < last; i++) {
        if (nums[i] > min) {
            return last - i + 1
        }
    }

    // return -1 if an error happens
    return -1
};

/*
Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0
*/