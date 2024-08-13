# leetcode problem # 40. Combination Sum II

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

"""
My solution: Bottom up

Idea: Find all the unique set of numbers adding up to each sum, up to the target
- The answer is the all unique sets adding up to the target

Runtime: O(N^2) where N is the number of candidates
Space: O(N^2)
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        while len(candidates) > 0 and candidates[-1] > target:
            candidates.pop()

        sums = [[] for _ in range(target + 1)]
        for candidate in candidates:
            newSets = [[] for _ in range(target + 1)]
            for idx in range(target - candidate + 1):
                for curSet in sums[idx]:
                    new = curSet[:]
                    new.append(candidate)
                    if new not in sums[idx + candidate]:
                        newSets[idx + candidate].append(new)

            new = [candidate]
            if new not in sums[candidate]:
                sums[candidate].append(new)
            for idx in range(target + 1):
                for newSet in newSets[idx]:
                    if newSet not in sums[idx]:
                        sums[idx].append(newSet)

        return sums[-1]
