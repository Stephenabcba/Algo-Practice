// leetcode problem #287. Find the Duplicate Number

/*
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
*/


/*
My solution: didn't work
Idea:
try to apply finding a single number that is duplicated exactly once to this problem

Problem:
The implementation of sums is inconclusive if the number appears more than 2 times
There is no way of knowing whether the number has appeared 3, 4, or more times

Potential alternative: brute force
- search through every number from 1 to n
- if the count of the number is more than 1, return the number
- result: O(N^2) runtime, O(1) space
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
    let theoreticalSum = 0
    let actualSum = 0
    for (let i = 0; i < nums.length; i++) {
        theoreticalSum += i
        actualSum += nums[i]
    }
    return actualSum - theoreticalSum
};

// Input: nums = [1,3,4,2,2]
// Output: 2

// Input: nums = [3,1,3,4,2]
// Output: 3

/*
Solution from leetcode: binary search on count
- if there were no repeated values (1,2,3...,n-1,n), the count of the number of values less than or equal to any given number k should be k
    - if some num x < 5 is duplicated, the count for k would be greater than k
    - thus, the duplicated value is the smallest number where its count is greater than itself
Implementation:
- The outer loop is a basic binary search logic
    - start begins at 1, end begins at n (nums.length - 1)
    - the middle is the truncated average of start and end
    - the inner loop finds the count of all numbers smaller or equal to middle
    - if the count is greater than mid, search to the left of mid
        - the duplicate might be the middle value
    - otherwise, search to the right of mid
- the last saved duplicate value is the smallest mid where count is greater than mid
*/
var findDuplicate2 = function (nums) {
    let start = 1
    let end = nums.length - 1
    let duplicate
    while (start <= end) {
        const mid = Math.floor((start + end) / 2)
        let count = 0
        for (let num of nums) {
            if (num <= mid) {
                count++
            }
        }
        if (count > mid) {
            duplicate = mid
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    return duplicate
};

/*
Alternative solutions on leetcode (overview)
* some algorithms do not meet constraints, and are listed for conceptual understanding
1. Sort then compare
    - *does not meet constraints (modifies original array)
2. Set and check if number already in set
    - *does not meet constraints (uses O(N) space)
3. Negative Marking
    - ex: if nums[0] is 3, change nums[3] to -nums[3] (nums[3] is also nums[nums[0]] in this case)
    - if nums[nums[i]] is already negative, nums[i] is repeated
    - *does not meet constraints (modifies original array)
4. Array as HashMap: treate the array as if it is a hashmap
    - iterative approach: swap nums[0] with nums[nums[0]]
        - if nums[0] === nums[nums[0]], nums[0] is duplicated
    - *does not meet constraints (modifies original array)
5. Binary Search (shown above)
6. Sum of Set Bits
    - initialize the answer to 0 (00000000... in binary)
    - for every binary bit where the sum at the bit for the array is greater than the sum at the bit for [1,n] (inclusive), set the answer at the bit to 1
    - after the operations, the decimal representation of answer is the duplicated value
7. Cycle detection
    - treat the nums array as an SLL
        - each index is a "node"
        - the value at the given index is the "next" of the "node"
        - ex: nums[9] = 5 -> the node at 9 has next of 5, the node at 5 has next of nums[5]
    - use the SLL cycle dectection to find the cycle 
        - runner (hare) will move 2 "nodes" every iteration
        - walker (tortoise) will move 1 "node" every iteration
        - where runner and walker meets denotes a cycle
        - after runner and walker meets, reset walker to the start, and runner moves 1 "node" at a time now
        - where runner and walker meets again is the entrance to the cycle, which is also the duplicated value
*/