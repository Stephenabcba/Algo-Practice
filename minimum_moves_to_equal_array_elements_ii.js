// leetcode problem # 462. Minimum Moves to Equal Array Elements II

/*
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.


Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:
Input: nums = [1,10,2,9]
Output: 16

Constraints:

n == nums.length
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
*/

/*
My solution: find the median then change all values to the median
Observation: in both test cases, the number of steps required matches that of changing all values to the median
- in the case of having even number of values in the array, the average of the center two values are taken
    - it is possible to have a non-whole number median in this case
        - however, rounding up or down to the closest whole number will suffice for this problem

Logic:
1. Find the median of the array
    - sort the array
    - find the center value (or floor the average of the center two values if the array has even number of values)
2. find the sum of the difference from each value to the median
3. return the sum

Runtime: O(N*Log N) where N is the number of items in the array
    - the sorting mechanism is the most time-intensive portion of the logic
Space: O(N) where N is the number of items in the array
    - this highly depends on the sorting used; if the sorting can be done in place, the space used is O(1)

Runtime performance of 132 ms (faster than 14.81%) and memory performance of 44.8MB (less than 6.17%) suggests that there are much more efficient algorithms.
- the performance gain is most likely in finding the median.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves2 = function (nums) {
    nums.sort((a, b) => a - b)


    let median
    if (nums.length % 2 === 0) {
        median = Math.floor((nums[nums.length / 2 - 1] + nums[nums.length / 2]) / 2)
    } else {
        median = Math.floor(nums[(nums.length - 1) / 2])
    }

    let ans = 0
    for (let num of nums) {
        ans += Math.abs(num - median)
    }

    return ans
};

/*
Improvement observed by referencing discussion and fastest performing JavaScript algorithms:
It doesn't matter that the values actually reach close to the median, as long as it reaches a center value
    - even for the case of array with even number of values where the center values are far apart, choosing any of the two center values as the centerpoint will
      yield the correct answer.

thus, the median is always:
let median = nums[Math.floor(nums.length / 2)]

The fastest performing algorithm(54ms) only had this noticeable change compared to my algorithm.
*/