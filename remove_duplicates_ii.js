// Leetcode problem #80. Remove Duplicates from Sorted Array II
// Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

// Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

// Return k after placing the final result in the first k slots of nums.

// Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

// Example 1:

// Input: 
const nums = [1,1,1,2,2,3]
// Output: 5, 
const expected = 5
const new_nums = [1,1,2,2,3]
// Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
// It does not matter what you leave beyond the returned k (hence they are underscores).

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let curNum = nums[0]
    let curNumCount = 1
    let k = 1
    let validNum = true
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] == curNum) {
            curNumCount ++
            if (curNumCount > 2) {
                validNum = false
            } else {
                k++
            }
        } else {
            curNum = nums[i]
            curNumCount = 1
            k++
            validNum = true
        }
        if (validNum && k <= i) {
            // console.log(`K: ${k}|I: ${i}`);
            nums[k-1] = nums[i]
        }
    }
    return k
};

console.log(removeDuplicates(nums));
console.log(nums);