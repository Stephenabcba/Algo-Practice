// leetcode problem #81. Search in Rotated Sorted Array II

/*
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
*/

/*
My Solution: using binary search after finding the pivot point
- iterate through the array to find the pivot point
    - when the number is smaller than the previous number, the pivot point is found
        - the current index is the start of the un-rotated index
- perform binary search with a twist
    - the variables stored are in relation to the un-rotated array
        - the start and end still initialized at 0 and end of array, but they are not directly related to indexes
            - the actual start is start + rotation index
            - the actual end is end + rotation index, normalized to be smaller than the length of the array
        - the middle is the truncated average of start and end
    - the actual mid index used to compare to the target is modified by the rotation, and normalized to be smaller than the length of the array
        - mid index = (middle + rotation index) % array length
        - if the number is found, return true
        - if the target is larger, search to the "right" of middle
            - start = middle + 1
        - if the target is smaller, search to the "left" of middle
            - end = middle - 1
- if the binary search loop condition ended, return false
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function (nums, target) {
    let rotation = 0
    let maxNum = nums[0]
    for (let i = 1; i < nums.length; i++) {
        if (maxNum > nums[i]) {
            rotation = i
            break
        } else {
            maxNum = nums[i]
        }
    }
    // console.log(rotation, nums[rotation]);
    const numsLength = nums.length
    let start = 0
    let end = numsLength
    while (start <= end) {
        // console.log("ok");
        let middle = Math.floor((start + end) / 2)
        let middleIndex = (middle + rotation) % numsLength
        if (nums[middleIndex] === target) {
            return true
        } else if (nums[middleIndex] < target) {
            start = middle + 1
        } else { // if (nums[middleIndex] > target)
            end = middle - 1
        }
    }
    return false
};

// Input: 
const nums = [2, 5, 6, 0, 0, 1, 2]
const target = 3
// Output: true

console.log(search(nums, target));

/*
Alternative solution on leetcode:
Idea:
- if the array is always pivoted, the nums array can be broken into 2 sorted arrays
    - all values in the first sorted array are always equal to or larger than every value in the second sorted array
    - if the start index is in the first sorted array, whether a value is in the first or second array is as follows:
        - compare the value at start index:
            - if the value at start index is larger: the value compared is in the second array
            - otherwise, the value compared is in the first array
        - if the start index is in the second sorted array, regular binary search logic is used
- if the target value and the middle index are both in the same array (both in first or both in second), regular binary search is used
- if the target value and middle index are in different arrays:
    - if middle index is in the first array: (then target is in second array)
        - search to the right of the middle index
    - if middle index is in the second array: (then target is in the first array)
        - search to the left of middle index
- caveat: if the start value is equal to the middle value, there's no way to tell whether the middle index is in the first or second array
    - the numbers have to be searched linearly until start value no longer equals middle value


*/

var search2 = function (nums, target) {
    // checks if the caveat, true if the value at start is not equal to the element
    const isBinarySearchHelpful = (arr, start, element) => {
        return arr[start] != element
    }

    // essentially, this function is used to check whether the target and middle value is in the same array
    // checks if the element is in the first sorted array
    //      returns true if the element is in the first array, false if the element is in the second array
    // this function will always return true once the start index is in the second sorted array
    //      the return value is incorrect, but the algorithm logic will just perform regular binary search
    const existInFirst = (arr, start, element) => {
        return arr[start] <= element
    }

    let n = nums.length;
    if (n === 0) return false;
    let start = 0;
    let end = n - 1;

    while (start <= end) {
        const mid = start + Math.floor(end - start) / 2;

        if (nums[mid] === target) return true;

        if (!isBinarySearchHelpful(nums, start, nums[mid])) {
            start++;
            continue;
        }

        // after this point:
        // - the middle value is not the target
        // - whether the middle value is in the first or second array is conclusive

        // checks if the value at middle index is in first array
        const pivotArray = existInFirst(nums, start, nums[mid]);
        // checks if the target value is in the first array
        const targetArray = existInfirst(nums, start, target);

        if (pivotArray !== targetArray) { // the two values are in different arrays
            if (pivotArray) { // the middle value is in the first array, thus the target is in the second array -> search to the right
                start = mid + 1;
            } else {// the middle value is in the second array, thus the target is in the first array -> search to the left
                end = mid - 1;
            }
        } else { // if both values are in the same array, just perform binary search
            if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
    }
    return false

};