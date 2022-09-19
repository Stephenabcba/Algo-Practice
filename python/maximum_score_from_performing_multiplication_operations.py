# leetcode problem # 1770. Maximum Score from Performing Multiplication Operations

"""
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.


Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 10^3
m <= n <= 10^5
-1000 <= nums[i], multipliers[i] <= 1000
"""

"""
My attempt: Attempting every every iteration with DP

The attempt used DP as suggested by hints on leetcode
Hint 1: At first glance, the solution seems to be greedy, but if you try to greedily take the largest value from the beginning or the end, this will not be optimal.
Hint 2: You should try all scenarios but this will be costy.
Hint 3: Memoizing the pre-visited states while trying all the possible scenarios will reduce the complexity, and hence dp is a perfect choice here.

However, the attempt still failed due to exceeding the time limit.
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp = {}

        def recurse(start, end, multipliersIndex):
            if multipliersIndex >= len(multipliers):
                return 0
            if (start, end) not in dp:
                chooseStart = nums[start] * multipliers[multipliersIndex] + \
                    recurse(start + 1, end, multipliersIndex + 1)
                chooseEnd = nums[end] * multipliers[multipliersIndex] + \
                    recurse(start, end - 1, multipliersIndex + 1)
                higher = max(chooseStart, chooseEnd)
                dp[(start, end)] = higher
            return dp[(start, end)]

        return recurse(0, len(nums) - 1, 0)


"""
Leetcode's implementation of recursive DP:
The right side can be calculated from (len(nums)-1)-(op-left), thus reducing the number of variables from 3 to 2.

Runtime: O(M^2) where M is the length of the multipliers array
Space: O(M^2) where M is the length of the multipliers array

However, the solution still received Time Limit Exceeded.
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)

        n = len(nums)

        memo = {}

        def dp(op, left):
            if op == m:
                return 0

            if (op, left) in memo:
                return memo[(op, left)]

            l = nums[left] * multipliers[op] + dp(op+1, left+1)
            r = nums[(n-1)-(op-left)] * multipliers[op] + dp(op+1, left)

            memo[(op, left)] = max(l, r)

            return memo[(op, left)]

        return dp(0, 0)


"""
Leetcode solution: Space-optimized Iterative DP

Similar to the recursive solution, the solution depends on changing the variables left and op, both of which can be in the range [0,m] (inclusive).
However, only squares where op >= left are valid since it's impossible to consume more values than the number of operations done
-> This reduces the problem space to half of the matrix.

Process the matrix from left to right, bottom to top and the solution can be found at dp[0][0]


As the results of each row only depends on the previously calculated row (the row below the current row), only 2 rows need to be saved at any given time
- This reduces the memory usage is reduced from a full matrix O(M^2) to 2 rows of the matrix O(M)

Runtime: O(M^2) where M is the length of the multipliers array
- The problem processes half of the matrix, which technically calculates O(M^2 / 2) iterations.
Space: O(M) where M is the length of the multipliers array
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        dp = [0] * (m+1)

        for op in range(m - 1, -1, -1):
            next_row = dp.copy()

            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])

        return dp[0]
