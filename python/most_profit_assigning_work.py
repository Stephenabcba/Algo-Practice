# leetcode problem # 826. Most Profit Assigning Work

"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

Example 2:
Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0

Constraints:
n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 10^4
1 <= difficulty[i], profit[i], worker[i] <= 10^5
"""

"""
My solution: Binary Search

Idea:
After sorting and mapping the proper profits for each job, each worker can find the most difficult job they can
complete with binary search

Logic:
1. Map the job difficulty to its pay with a dictionary
    * multiple jobs could share the same difficulty, in which case the highest pay is taken
2. Sort the jobs by their difficulty
3. Correct any profit inconsistencies
    - there could be job with difficulty 1 with pay of 100 and another job with difficulty of 100 with pay of 1
    -> set the pay of each job to the highest pay seen up to the current point
        - for the case above, the job with difficulty of 100 would also have a pay of 100
4. Find the most difficult job each worker can complete with binary search
5. Return the total profit made

Runtime: O(N * logN + M * logN) where N is the length of difficulty list, and M is the length of worker list
Space: O(N)
"""


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        N = len(difficulty)
        highestProfits = {}

        def binarySearch(target):
            low = -1
            high = N - 1

            while low < high:
                mid = math.ceil((low + high) / 2)
                if target < difficulty[mid]:
                    high = mid - 1
                else:
                    low = mid
            if high < 0:
                return 0
            return highestProfits[difficulty[high]]

        for idx in range(N):
            if difficulty[idx] not in highestProfits:
                highestProfits[difficulty[idx]] = profit[idx]
            else:
                if profit[idx] > highestProfits[difficulty[idx]]:
                    highestProfits[difficulty[idx]] = profit[idx]

        difficulty.sort()
        curPay = 0
        for diff in difficulty:
            if highestProfits[diff] < curPay:
                highestProfits[diff] = curPay
            else:
                curPay = highestProfits[diff]

        ans = 0

        for w in worker:
            ans += binarySearch(w)

        return ans


"""
From Editorial: Memoization

Idea: Find the pay for every possible difficulty in the range from 1 to the highest worker ability

Time complexity: O(n + m + maxAbility)
Space complexity: O(maxAbility)
** In python3, this solution performs worse in both runtime and memory than binary search
"""


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # Find maximum ability in the worker array.

        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)

        for i in range(len(difficulty)):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        # Take maxima of prefixes.

        for i in range(1, maxAbility + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])
        netProfit = 0
        for ability in worker:
            netProfit += jobs[ability]
        return netProfit
