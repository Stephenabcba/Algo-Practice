# leetcode problem # 1046. Last Stone Weight

"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

"""
My solution: Heap

Observation: The data structure should remain sorted even when items are added
and removed from it
-> a heap can be used to achieve this
    - adding and removing values from the heap take O(logN) time
    * as Python's built in heap is a min heap, values are inserted as
    their negative counterparts to achieve the function of a max heap

Logic: follow the rules
1. convert the list into a heap
2. repeat until at most 1 stone is left:
    - pop 2 stones from the heap
    - if the stones have different weight, insert the difference back into the heap
3. if there is 1 stone left, return the weight of the stone
4. otherwise, return 0

Runtime: O(N * logN) where N is the number of stones
Space: O(1), the heap is done in-place with the input list, thus not using extra space
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx in range(len(stones)):
            stones[idx] = - stones[idx]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)

        if stones:
            return -stones[0]

        return 0
