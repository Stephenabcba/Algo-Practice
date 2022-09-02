// leetcode problem # 1480. Running Sum of 1d Array

/*
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
*/

/*
My solution:
calculate the running sum and store the values in a new array.

It is also possible to calculate the running sum in the input array (no extra space)
the value at each index is simply current val + the value of the previous index (iterating from the front)
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
    const ans = []
    let sum = 0
    for (let num of nums) {
        sum += num
        ans.push(sum)
    }
    return ans
};

/*

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
*/