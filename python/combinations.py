# leetcode problem # 77. Combinations

"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""

"""
My solution: Recursion

Since combinations are unordered, the values in the list can be arranged in order while including
all the possible combinations
    - ex. [2,1] can be rearranged to [1,2] without removing from the solution
-> if each combination's values are arranged in order, in a single combination, any value within the 
    list is greater than the values before it

If k is fixed for all inputs, the solution could be created by writing k for-loops, each loop adding
a new value to the combination
- the start of each loop is 1 larger than the parent loop
- the end of each loop is n - the number of values to be added + 2

However, as k is variable from 1 to n, the solution cannot be a fixed number of nested loops
-> using recursion, the number of loops can effectively be variable by recursing every time
a loop is needed

=> Solution: use recursion to create nested for-loops that can build the combinations, with each loop
starting at 1 larger than the value of the parent loop

Space: O(1) The logic does not use extra space that scales with input except for the answer list
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def generate(start, end, generateCount, curCombo):
            if start + generateCount > end:
                return
            curCombo.append(start)
            generateCount -= 1
            if generateCount == 0:
                ans.append(curCombo)
            else:
                for newStart in range(start + 1, end - generateCount + 1):
                    generate(newStart, end, generateCount, curCombo.copy())

        for start in range(1, n - k + 2):
            generate(start, n + 1, k, [])

        return ans