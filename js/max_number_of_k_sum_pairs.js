// leetcode problem #1679. Max Number of K-Sum Pairs

/* 
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
*/

/*
My solution: repeated 2-sum solution
A greedy solution works here because removing a pair of numbers does not change the solution.
    - for example, if  nums=[1,1,2,5] and k=6, removing the first 1 or the second 1 does not matter
        - either way, the array after the operation will be [1,2]

In this solution, the nums array is sorted first, then the solution is searched with a 2-pointer approach

Runtime: O(N* log(N)), or the runtime of the sorting algorithm
Space: O(1), unless the sorting algorithm takes more space.

The solution can potentially be done with a hash table.
    - find the count of each value and store it in a hash table
    - for each number x in the array, look for its count and its complement y (where x + y = k)
        - add the smaller count to the total and set both counts to 0 in the hash table
    - O(N) in both runtime and space.
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function (nums, k) {
    nums.sort((a, b) => a - b)

    let front = 0
    let back = nums.length - 1
    let operations = 0

    while (front < back) {
        let sum = nums[front] + nums[back]
        if (sum > k) {
            back--
        } else if (sum < k) {
            front++
        } else {
            operations++
            front++
            back--
        }
    }
    return operations
};

/*
Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
*/