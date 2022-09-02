// leetcode problem # 377. Combination Sum IV

/*
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.


Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
*/

/*
Solution by amanahlawat in leetcode discussions: Dynamic programming with DFS

Idea:
Starting from a sum of 0, recursively explore whether adding any of the values in the nums array could reach the target
- Recursion set up:
    - base cases
        1. the sum reached target (sum == target); the path taken to reach the target is one valid way.
        2. the sum overshot the target (sum > target); the path taken to reach the target is invalid
    - recursive case
        - the sum has not reached the target (sum < target)
            - for each number in the nums array, recursively explore if sum + num could reach target.
- For the example case of [1,2,3] with a target of 4:
    - start from sum of 0
    - add any of the numbers to the sum
    - recursively add different values until the base case is reached
    * for the example below, the sums over the target are skipped.
                 0
         /       |        \
    1             2            3
   / \  \        /  \          |
  2   3  4      3   4          4
 / \  |         |
3  4  4         4
|
4

As seen above, when the sum is 2, there's always 2 ways of reaching the target of 4
When the sum is 3, there's always 1 way of reaching the target of 4


In order to reduce redundant calculations, a dynamic programming array can be used.
- As observed above, at a given sum, there's a fixed number of ways to reach the target with the given inputs.
    - Therefore, the number of ways can be saved to the DP array (at the index of the given sum)
- When another path of recursion has reached a sum previously reached, the results can be taken from the DP array, insteading of repeating unnecessary recursion

Runtime: O(N * M) where N is the length of the nums array and M is the target value
- In the worst case, the nums array has 200 values (with 1 as part of the values) and target is 1000
    - in the first 1000 recursions, the algorithm will keep adding 1 to the sum until it reaches 1000
    - in the next 199 recursion, the algorithm will explore the other 199 numbers when the sum is 999
    - and in the next ~199,000 recursions, the alorithm will explore the 199 numbers when the sum is 998, 997... 0
Space: O(L) where L is the max limit of target value
- Note that the memory usage depends on problem constraints, not the function input

Thoughts to follow up:
if negative numbers are allowed, a cycle can be created, which could potentially have infinite number of combinations
- ex: if 1 and -1 exists, the sum could infintiely be +1 then -1, reaching a net change of 0
- two different ways of securing problem boundaries are to limit the usage of each negative number to only once, or limit the total number of values included in each sum.
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function (nums, target) {
    let dp = new Array(1001).fill(-1)
    let recurse = (curSum) => {
        // the path overshot; it is not a valid path
        if (curSum > target) return 0
        // the path reached target; it is a valid path
        if (curSum == target) return 1
        // the path reached a sum that has been previously reached, the path will always have dp[curSum] ways to reach the sum.
        if (dp[curSum] != -1) return dp[curSum]

        let ways = 0
        for (let i = 0; i < nums.length; i++) {
            if (curSum + nums[i] <= target) {
                ways += recurse(curSum + nums[i])
            }
        }
        // save the number of ways to reach the target from the current sum to the dp array
        dp[curSum] = ways
        return ways
    }
    // the answer is all the ways that the target can be reached from the starting sum of 0.
    return recurse(0)
};