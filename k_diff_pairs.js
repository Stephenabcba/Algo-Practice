// Leetcode problem #532. K-diff Pairs in an Array
// Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

// A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

// 0 <= i < j < nums.length
// |nums[i] - nums[j]| == k
// Notice that |val| denotes the absolute value of val.

// Example 1:

// Input: 
const nums = [3,1,4,1,5], k = 2
// Output: 
const output = 2
// Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
// Although we have two 1s in the input, we should only return the number of unique pairs.

// Example 2:

// Input: 
const nums2 = [1,2,3,4,5], k = 1
// Output: 
const output2 = 4
// Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    let uniquePairCount = 0;
    if (k == 0) {
        let freqTable = {};
        for (let num of nums) {
            if (freqTable.hasOwnProperty(num)) {
                if (freqTable[num] === 1) {
                    uniquePairCount++
                }
                freqTable[num]++
            } else {
                freqTable[num] = 1
            }
        }
        return uniquePairCount
    }
    let numSet = new Set(nums)
    for (let num of numSet) {
        if (numSet.has(num+k)) {
            uniquePairCount++;
        }
    }
    return uniquePairCount
};