// leetcode problem #905. Sort Array By Parity

/*
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
*/

/*
My solution: separate the odds and evens separately and sort, and then concat
Runtime: O(N* log N), or the efficiency of the sorting algorithm
Space: O(N), the evens and odds array will take up O(N) space, and the return array also takes up O(N) space.
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function (nums) {
    const evens = []
    const odds = []
    for (let num of nums) {
        if (num % 2 == 0) {
            evens.push(num)
        } else {
            odds.push(num)
        }
    }
    evens.sort((a, b) => a - b)
    odds.sort((a, b) => a - b)
    return evens.concat(odds)
};

/*
Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
*/