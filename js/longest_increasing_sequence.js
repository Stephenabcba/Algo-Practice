// leetcode problem # 300. Longest Increasing Subsequence

/*
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
*/

/*
My solution: keep track of the length of the chains
For each num, attack to the longest chain that ends with a value smaller than num

Runtime: O(N^2) where N is length of nums array
Space: O(N) where N is length of nums array
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
    let dp = new Array(nums.length).fill(1)
    let max = 1
    let maxChain = 1
    for (let i = 1; i < nums.length; i++) {
        maxChain = 0
        for (let j = i - 1; j >= 0; j--) {
            if (nums[j] < nums[i]) {
                maxChain = Math.max(maxChain, dp[j])
            }
        }
        dp[i] = maxChain + 1
        if (dp[i] > max) {
            max = dp[i]
        }
    }
    return max
};

/*
Solution in leetcode discussion by warrenruud
Create a new array
1. if a value is larger than the last value in the array, add it to the array
2. if a value is smaller than the last value in the array, replace the smallest value larger than it in the array
- this can be done using binary search

*Note that the values in the array may not correspond to the values in the LIS

Runtime: O(N * logN) where N is the length of the nums array
Space: O(N) where N is the length of the nums array
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
    let arr = [nums[0]]
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > arr[arr.length - 1]) {
            arr.push(nums[i])
        } else {
            let start = 0
            let end = arr.length - 1

            let middle
            while (start < end) {
                middle = Math.floor((start + end) / 2)
                if (nums[i] > arr[middle]) {
                    start = middle + 1
                } else {
                    end = middle
                }
            }
            arr[start] = nums[i]
        }
    }
    return arr.length
};