# leetcode problem # 2279. Maximum Bags With Full Capacity of Rocks

"""
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.


Example 1:
Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Output: 3
Explanation:
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.

Example 2:
Input: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
Output: 3
Explanation:
Place 8 rocks in bag 0 and 2 rocks in bag 2.
The number of rocks in each bag are now [10,2,2].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that we did not use all of the additional rocks.

Constraints:
n == capacity.length == rocks.length
1 <= n <= 5 * 10^4
1 <= capacity[i] <= 10^9
0 <= rocks[i] <= capacity[i]
1 <= additionalRocks <= 10^9
"""

"""
My Solution: find the rocks needed and sort

Intuition:
Filling the bags that need the least rocks to be full yields the most bags filled

Logic:
1. Iterate through each bag
- find the number of rocks required to filled each bag (required = capacity - current rocks)
- if the bag is already full, increment the full bag count
- otherwise, required rock count of the bag to a list
2. Sort the list from largest to smallest
3. Iterate through the list, popping 1 item at a time
- take rocks out of the additional rocks pile until the bag is filled
- if the bag is filled, increment the full bags count
- continue until either additional rocks are all used or there's no more bags to fill
4. return the full bag count

Runtime: O(N) where N is the number of "bags" (length of capacity list or rocks list)
Space: O(N)
"""


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        fullBags = 0
        neededStones = []
        for idx in range(len(capacity)):
            missingStoneCount = capacity[idx] - rocks[idx]
            if missingStoneCount == 0:
                fullBags += 1
            else:
                neededStones.append(missingStoneCount)

        neededStones.sort(reverse=True)

        while additionalRocks > 0 and fullBags < len(capacity):
            stoneReq = neededStones.pop()
            print(stoneReq)
            if stoneReq <= additionalRocks:
                additionalRocks -= stoneReq
                fullBags += 1
            else:
                break
        return fullBags
