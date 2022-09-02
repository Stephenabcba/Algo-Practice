// leetcode problem # 34. Find First and Last Position of Element in Sorted Array

/*
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
*/

/*
My solution: Binary search up to 3 times

As nums is a non-decreasing array, binary search can be utilized.

The first binary search looks for the existence of target
- if target is found, move to the next step
- if target is not found, the answer is [-1,-1]

If target was found, perform 2 additional binary searches to find the start and end index of target.
- the two searches can continue with the reduced range from the first binary search

Runtime: O(log N) where N is the length of nums array
Memory: O(1) Logic memory usage does not scale with input size
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
    let start = 0
    let end = nums.length - 1
    let middle

    let numStart = -1
    let numEnd = -1

    // find the first occurrence of target
    while (numStart < 0 && start <= end) {
        middle = Math.floor((start + end) / 2)
        if (nums[middle] > target) {
            end = middle - 1
        } else if (nums[middle] < target) {
            start = middle + 1
        } else {
            numStart = middle
            numEnd = middle
        }
    }

    // expand the range of answer if target was found
    if (numStart >= 0) {
        // find the start index of target in nums
        let targetStartLower = start
        let targetStartUpper = numStart

        while (targetStartLower <= targetStartUpper) {
            middle = Math.floor((targetStartLower + targetStartUpper) / 2)
            if (nums[middle] < target) {
                targetStartLower = middle + 1
            } else if (nums[middle] == target) {
                targetStartUpper = middle - 1
                numStart = middle
            } else {
                console.log("Problem: found greater number in lower end")
                break
            }
        }

        // find the end index of target in nums
        let targetEndLower = numEnd
        let targetEndUpper = end

        while (targetEndLower <= targetEndUpper) {
            middle = Math.floor((targetEndLower + targetEndUpper) / 2)
            if (nums[middle] > target) {
                targetEndUpper = middle - 1
            } else if (nums[middle] == target) {
                targetEndLower = middle + 1
                numEnd = middle
            } else {
                console.log("Problem: found lower number in upper end")
                break
            }
        }
    }

    return [numStart, numEnd]
};