# leetcode problem # 1743. Restore the Array From Adjacent Pairs

"""
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.


Example 1:
Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.

Example 2:
Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.

Example 3:
Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]

Constraints:
nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 10^5
-10^5 <= nums[i], ui, vi <= 10^5
There exists some nums that has adjacentPairs as its pairs.
"""

"""
My solution: Chain the pairs

Logic:
1. Place the pairs into dictionary
- if a is a pair with b, a should be in the entry of b and b should be in the entry of a
2. Find the start of the chain
- the start of the chain is an entry in the dictionary with only one paired value
    - the end of the chain also has only one paired value
        - however, the problem accepts nums in both directions, so it doesn't matter which one is picked
3. Build the chain
- traverse the dictionary using the pairs
- always follow the pair that has not been used yet
4. Return the completed chain

Runtime: O(N) where N is the length of the original nums list
Space: O(N)
"""


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacentDict = defaultdict(list)

        for a, b in adjacentPairs:
            adjacentDict[a].append(b)
            adjacentDict[b].append(a)

        ans = []

        for num in adjacentDict:
            if len(adjacentDict[num]) == 1:
                ans.append(num)
                prev = num
                cur = adjacentDict[num][0]
                ans.append(cur)
                while len(adjacentDict[cur]) > 1:
                    for val in adjacentDict[cur]:
                        if val != prev:
                            prev = cur
                            cur = val
                            ans.append(val)
                            break
                break

        return ans
