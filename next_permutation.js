// leetcode problem # 31. Next Permutation
/*
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
*/

/*
My solution: based on a pattern observed
- Pattern:
    - starting from the back of nums array, a key target index is present at the first index that breaks the non-decreasing order
    - the value at the target index is swapped with the smallest value greater than nums[target] in the subarray from target + 1 to end of nums array
        - if the smallest greater value is duplicated, the number that is closer to the smallest value of the subarray is used for the swap
    - the subarray is sorted from smallest to largest
- Implementation:
    - find the first value from the back where it is strictly smaller than the value at its index + 1
        - this is the target index (targetIndex)
    - "sort" the subarray at indexes [targetIndex + 1, nums.lenth-1] (inclusive)
        - for optimization, the subarray only needs to be reversed since the subarray was in non-decreasing order
    - starting at targetIndex + 1, find the first value in the subarray that is strictly larger than nums[targetIndex]
        - swap nums[targetIndex] with the value found

Runtime: O(N), all iterations basically run parallel to each other
    - the full array reversal is run at most 1 time in the first while loop
Space: O(1), the memory used does not scale with size of the array at all.
*/


/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function (nums) {
    if (nums.length === 1) {
        return
    }
    let targetIndex = nums.length - 2
    let swapped = false
    // find the largest subarray in nums (that starts at the end of nums) that is in the largest lexicographical order
    while (nums[targetIndex] >= nums[targetIndex + 1]) {
        if (targetIndex === 0) { // if (the array is in its largest lexicographical order, reversing the array returns the smallest lexicographical order)
            for (let i = 0; i < nums.length / 2; i++) {
                let temp = nums[i]
                nums[i] = nums[nums.length - 1 - i]
                nums[nums.length - 1 - i] = temp
            }
            return
        }
        targetIndex--
    }
    // "sort" the subarray from smallest to largest
    // since the subarray is already sorted from largest to smallest, only a reversal is required
    for (let i = targetIndex + 1; i < (nums.length + targetIndex) / 2; i++) {
        let temp = nums[i]
        nums[i] = nums[nums.length - (i - targetIndex)]
        nums[nums.length - (i - targetIndex)] = temp
    }
    let nextSmallest = targetIndex + 1
    while (nextSmallest < nums.length - 1 && nums[nextSmallest] <= nums[targetIndex]) {
        nextSmallest++
    }
    let temp = nums[nextSmallest]
    nums[nextSmallest] = nums[targetIndex]
    nums[targetIndex] = temp
};

// TEST CASES
//            0  1  2  3  4  5  6  7
const nums = [1, 1, 2, 2, 3, 3, 4, 4]
// const nums = [1, 2, 3, 4]
// const nums = [1, 1, 5]
console.log(nums);
for (let i = 0; i < 20; i++) {
    nextPermutation(nums)
    console.log(nums);
}

/*
Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
*/