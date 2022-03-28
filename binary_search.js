// leetcode problem #704. Binary Search
/*
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
*/

/*
My solution: basic binary search implementation
- initialize start and end index at the start and end of the nums array, respectively
- repeat the following until the start is larger than the end, or the number is found
    - the middle is the index that is the average of the start and end index (decimal values truncated)
    - compare the number at the middle index to the target
        - if they are equal, return the middle index
        - otherwise, if the number at the middle index is smaller than target, move the start index to middle index + 1
        - otherwise, the number at the middle index is larger than the target; move the end index to middle index - 1
- binary search effectively cuts the search space by half every iteration, thus resulting in O(log N) time complexity for N numbers
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let start = 0
    let end = nums.length - 1
    while (start <= end) {
        const middle = Math.floor((start + end) / 2)
        if (nums[middle] === target) {
            return middle
        } else if (nums[middle] < target) {
            start = middle + 1
        } else { // if (nums[middle] > target)
            end = middle - 1
        }
    }
    return -1
};

const nums = [-1, 0, 3, 5, 9, 12]
const target = 9

const nums2 = [-1, 0, 3, 5, 9, 12]
const target2 = 2

console.log(search(nums2, target2))