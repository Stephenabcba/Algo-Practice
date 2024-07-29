# leetcode problem # 1395. Count Number of Teams

"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4

Constraints:
n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
All the integers in rating are unique.
"""

"""
My solution: Split up Brute Force

Note: In full brute force solution, 3 nested loops are used
- The runtime of this approach is O(N^3)
- The space of this approach is O(1)
- The brute-force solution results in Time Limit Exceeded error

To reduce the runtime, a tradeoff is made to increase the space useage
-> the three nested loops could be split up into two nested loops
    - First nested loop find all pairs (i,j) where ratings[i] < ratings[j] or ratings[i] > ratings[j]
        - The pairs are saved in two lists, largerThan and smallerThan
        - for each pair found, increment the value at index j of the pair
            - if ratings[i] < ratings[j], increment smallerThan
            - otherwise, increment largerThan
    - Second nested loop finds all pairs (j,k) where ratings[j] < ratings[k] or ratings[j] > ratings[k]
        - Using largerThan and smallerThan, trios can be formed
            - if ratings[j] < ratings[k], the number of trios formed is smallerThan[j]
            - if ratings[j] > ratings[k], the number of trios formed is largerThan[j]
    - Count the number of trios formed and return the value


Runtime: O(N^2) where N is the number of ratings
Space: O(N)
"""


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        print(n)
        teams = 0
        largerThan = [0] * n
        smallerThan = [0] * n
        for idx in range(n - 1):
            for jdx in range(idx + 1, n):
                if rating[idx] < rating[jdx]:
                    smallerThan[jdx] += 1
                else:
                    largerThan[jdx] += 1

        for jdx in range(1, n - 1):
            for kdx in range(jdx + 1, n):
                if rating[jdx] < rating[kdx]:
                    teams += smallerThan[jdx]
                else:
                    teams += largerThan[jdx]

        return teams
