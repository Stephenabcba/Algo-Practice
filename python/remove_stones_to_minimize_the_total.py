# leetcode problem # 1962. Remove Stones to Minimize the Total

"""
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).


Example 1:
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Example 2:
Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.

Constraints:
1 <= piles.length <= 10^5
1 <= piles[i] <= 10^4
1 <= k <= 10^5
"""

"""
My solution: Use heap

Intuition: Always remove stones from the largest pile
- floor(piles[i] / 2) is the largest when piles[i] is the largest in piles

In order to find the largest pile every time, a heap can be used
- removing and inserting items in a heap takes O(logN) time
- in Python, heapq is a minheap, so the values in the pile are inserted as negative numbers to create a max heap
    - as the numbers are negative, ceiling function is used instead of floor function

Runtime: O(N + k * logN) where N is the length of piles list, and k is input integer k
Space: O(N)
"""


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for idx in range(len(piles)):
            piles[idx] = - piles[idx]
        heapq.heapify(piles)

        for operation in range(k):
            heapq.heappushpop(piles, piles[0] - ceil(piles[0] / 2))

        return - sum(piles)
