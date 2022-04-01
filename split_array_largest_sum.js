// leetcode problem # 410. Split Array Largest Sum

/*
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
*/

/*
Solution from Leetcode solution
* leetcode's basic solution was dynamic programming
    - can be done either through recursive (with memoization) or iterative approach
    - calculate the minumum sum for every split and every location
Best Solution: Binary search
Idea:
- the minimum largest sum is between the largest value within the nums array and the sum of the nums array
    - start range for binary search is the largest value of nums array
    - end range for binary search is the sum of the nums array
- using priciples of binary search, the search range can be halved each iteration
    - it is assumed that the minimum sum is at the highest end of the range at the beginning
    - the binary search will always run until the end

Logic:
for the binary search:
    - the "target sum" is the truncated average of the current min and max range of binary search
    - each iteration, calculate the number of subarrays required to reach the target sum
    - if the number of subarrays is lower than or equal to M, lower the minimum largest sum to the current target sum
    - the start and end range is moved accordingly

runtime: O(N * log(S)), where N is the number of values in nums array, and S is the sum of values in nums array
*/

/**
 * @param {number[]} nums
 * @param {number} m
 * @return {number}
 */
var splitArray = function (nums, m) {
    // from solution
    const minSubarraysRequired = (maxSumAllowed) => {
        let curSum = 0
        let splitsRequired = 0

        for (const element of nums) {
            if (curSum + element <= maxSumAllowed) {
                curSum += element
            } else {
                // make a new split
                curSum = element
                splitsRequired++
            }
        }
        // the number of subarrays is 1 more than the number of splits
        return splitsRequired + 1
    }

    let sum = 0
    let max = 0
    for (const element of nums) {
        sum += element
        max = (element > max) ? element : max
    }

    let start = max
    let end = sum
    let minLargestSplitSum = -1
    while (start <= end) {
        let maxSumAllowed = Math.floor((start + end) / 2)

        if (minSubarraysRequired(maxSumAllowed) <= m) {
            end = maxSumAllowed - 1
            minLargestSplitSum = maxSumAllowed
        } else {
            start = maxSumAllowed + 1
        }
    }
    return minLargestSplitSum
};