# leetcode problem # 2285. Maximum Total Importance of Roads

"""
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.

Example 1:
https://assets.leetcode.com/uploads/2022/04/07/ex1drawio.png
Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.

Example 2:
https://assets.leetcode.com/uploads/2022/04/07/ex2drawio.png
Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20
Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
- The road (0,3) has an importance of 4 + 5 = 9.
- The road (2,4) has an importance of 2 + 1 = 3.
- The road (1,3) has an importance of 3 + 5 = 8.
The total importance of all roads is 9 + 3 + 8 = 20.
It can be shown that we cannot obtain a greater total importance than 20.

Constraints:
2 <= n <= 5 * 10^4
1 <= roads.length <= 5 * 10^4
roads[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no duplicate roads.
"""

"""
My solution: Count then sort

Idea: Assign values to cities based on the number of roads they're connected to
- If a city has X connections, it will contribute its value to the total importance X times
    -> Cities with more connections should have higher value
- If two cities have the same amount of connections, the order of assigning values to them is arbitrary for this problem
    - ex: if city A and city B both have 3 connections, it doesn't matter if A has a value of 4 (while B has 5) or B has a value of 4 (while A has 5)
        - in both cases, both cities will produce a combined importance of 27
- To properly assign values, count the number of roads connected to each city, then sort the cities based on their connections
    - the city with the least connections gets a value of 1, and the city with the most connections get a value of n
- The total importance value is the sum of (each city's connected roads count * the city's assigned value)

Runtime: O(N * logN + M) where N is the number of cities, and M is the number of roads
Space: O(N)
"""


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connections = [0] * n

        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1

        connections.sort()

        ans = 0

        for point in range(1, n + 1):
            ans += connections[point - 1] * point

        return ans
