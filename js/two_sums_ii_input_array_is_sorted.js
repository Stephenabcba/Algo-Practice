// leetcode problem # 167. Two Sum II - Input Array Is Sorted

/*
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Constraints:

2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
*/

/*
My solution: Two pointers
A standard two-sum problem with a sorted array can be solved as follows:
1. Initialize two pointers to the array, one pointer pointing at the start and the other pointing at the end.
2. Find the sum of the values at both pointers.
    - if the sum is too large, decrement the back pointer
        - as the array is sorted, doing so will decrease the sum (going "left" in a sorted array decreases the value)
    - if the sum is too small, increment the front pointer
        - as the array is sorted, doing so will increase the sum (going "right" in a sorted array increases the value)
3. Repeat step 2 until the sum is found

As JS is a 0-indexed language, the solutions need to add 1 to return the 1-indexed answer the problem requested.

Runtime: O(N) where N is the length of numbers array. Each value is processed at most once.
Space: O(1) The solution does not scale with input size in terms of memory.
*/

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
    let smallIndex = 0
    let largeIndex = numbers.length - 1
    let sum = numbers[smallIndex] + numbers[largeIndex]

    while (sum != target) {
        if (sum < target) {
            smallIndex++
        } else if (sum > target) {
            largeIndex--
        }
        sum = numbers[smallIndex] + numbers[largeIndex]
    }

    return [smallIndex + 1, largeIndex + 1]
};

/*

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

*/