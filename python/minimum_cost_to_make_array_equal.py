# leetcode problem # 2448. Minimum Cost to Make Array Equal

"""
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

Example 1:
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.

Example 2:
Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.

Constraints:
n == nums.length == cost.length
1 <= n <= 10^5
1 <= nums[i], cost[i] <= 10^6
"""

"""
My solution: Sort then calculate cost

Observation: the minimum cost will always occur on a value already in nums
    - if the minimum cost can occur in a value in between two numbers in nums, then the cost to change is 0
    at that point, and can move to a number in nums for no cost.
-> only need to consider values already in nums

Intuition: After sorting nums, find the cost to move to each number in nums
    - the cost is the sum of increasing all all values below num and decreasing all values above num
        - keep track of the unit cost of increasing/decreasing during iteration, and the 
        - do two passes to get the costs of increasing and decreasing respectively
-> the answer is the minimum of the costs


Runtime: O(N*logN) where N is the length of nums list
    Sorting takes O(N*logN) time
    The rest of the algorithm takes O(N) time
Space: O(N)
"""

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        costPerChange = 0
        totalCost = 0

        zippedNumsSorted = sorted(zip(nums,cost))
        
        prevNum = zippedNumsSorted[0][0]
        cumulativeCosts = []

        for num, cost in zippedNumsSorted:
            totalCost += costPerChange * (num - prevNum)
            cumulativeCosts.append(totalCost)
            prevNum = num
            costPerChange += cost

        totalCost = 0
        costPerChange = 0
        prevNum = zippedNumsSorted[-1][0]

        minCost = float('inf')

        for idx in range(len(zippedNumsSorted) - 1, -1, -1):
            totalCost += costPerChange * (prevNum - zippedNumsSorted[idx][0])
            cumulativeCosts[idx] += totalCost
            if cumulativeCosts[idx] < minCost:
                minCost = cumulativeCosts[idx]
            prevNum = zippedNumsSorted[idx][0]
            costPerChange += zippedNumsSorted[idx][1]
        
        return minCost
