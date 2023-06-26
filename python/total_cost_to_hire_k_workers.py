# leetcode problem # 2462. Total Cost to Hire K Workers

"""
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

Example 1:
Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

Example 2:
Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.

Constraints:
1 <= costs.length <= 10^5 
1 <= costs[i] <= 10^5
1 <= k, candidates <= costs.length
"""

"""
My solution: 2 heaps

Idea:
1. Have a group each for the first and last x candidates
2. for each hiring round, compare the lowest cost candidates from the front and the back groups
    - hire the lower cost of the 2 candidates
    - add 1 more candidate to the group if possible to maintain x candidates in the pool
3. repeat for k rounds 

Edge case: When the front and back candidate pools overlap
-> only include the overlapped candidates once, either to the front or the back
    - for the sake of the solution, it doesn't matter if the candidate is added to the front of the back
- there's no need to add more candidates to the pools after hiring, as all the candidates are considered
- when this edge case happens, it's also possible that eventually the front or the back pool of candidates
    become empty
    -> only consider the non-empty pool for hiring

To find the lowest cost in the pool for multiple rounds while adding more candidates to the pool, a heap
can be used to maintain order where the smallest value can be found in O(1) time and values can be removed
or added in O(logN) time.

Runtime: O(N + M * logN) where N is the number of candidates to consider each round and M is the number of hires
    - it takes O(N) to convert an array to a heap
    - there are M rounds of hiring, each taking logN time to hire a condidate and update the heap
Space: O(N)
    - it takes N spaces to create a heap, and there are 2 heaps
"""

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        frontLast = candidates
        backFirst = max(len(costs) - candidates, frontLast)

        frontHeap = costs[:frontLast]
        backHeap = costs[backFirst:]

        heapq.heapify(frontHeap)
        heapq.heapify(backHeap)

        totalCost = 0

        while k > 0:
            if len(frontHeap) == 0:
                for idx in range(k):
                    totalCost += heapq.heappop(backHeap)
                k = 0
            elif len(backHeap) == 0:
                for idx in range(k):
                    totalCost += heapq.heappop(frontHeap)
                k = 0
            elif frontHeap[0] <= backHeap[0]:
                if frontLast < backFirst:
                    totalCost += heapq.heapreplace(frontHeap, costs[frontLast])
                    frontLast += 1
                else:
                    totalCost += heapq.heappop(frontHeap)
                k -= 1
            else:
                if frontLast < backFirst:
                    totalCost += heapq.heapreplace(backHeap, costs[backFirst - 1])
                    backFirst -= 1
                else:
                    totalCost += heapq.heappop(backHeap)
                k -= 1
        return totalCost