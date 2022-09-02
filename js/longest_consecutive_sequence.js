// leetcode problem #128. Longest Consecutive Sequence

/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
*/

/*
I was able to utilize sorting (O(N log N) time) to solve this problem, but was unable to create a O(N) solution.
*/

/*
Solution from leetcode solutions: utilize set / hashset
intuition from improving the brute force method:
- in the brute force method, the algorithm iterates through each number and attempts to find consecutive sequences for each number
    - however, the method requires O(N^3) time as it linear searches for the consecutive sequences each time
- improvement: use a set to keep track of each value
    - as the problem definition does not explicitly limit memory usage, a more memory intensive data structure can be used
    - by using a hashset, the lookup required in the brute force method becomes O(1)
    - optimization:
        - by only considering values that are start of a consecutive sequence (num - 1 does not exist in the set), the inner loop processes each value in the set exactly once (instead of nested loops)
Runtime: O(N), where N is the length of nums array.
    - although there is a nested loop, the inner loop does not run for every iteration of the outer loop.
        - the inner loop will process each number in the set exactly once
Space: O(N), where N is the length of nums array
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
    let num_set = new Set()
    for (let num of nums) {
        num_set.add(num)
    }

    let longestStreak = 0

    for (let num of num_set) {
        // only execute if current number is start of a consecutive sequence
        if (!num_set.has(num - 1)) {
            let currentNum = num
            let currentStreak = 1

            while (num_set.has(currentNum + 1)) {
                currentNum += 1
                currentStreak += 1
            }

            longestStreak = Math.max(currentStreak, longestStreak)
        }
    }

    return longestStreak
};