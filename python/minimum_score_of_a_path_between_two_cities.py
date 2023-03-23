# leetcode problem # 2492. Minimum Score of a Path Between Two Cities

"""
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.

Example 1:
https://assets.leetcode.com/uploads/2022/10/12/graph11.png
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:
https://assets.leetcode.com/uploads/2022/10/12/graph22.png
Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

Constraints:
2 <= n <= 10^5
1 <= roads.length <= 10^5
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 10^4
There are no repeated edges.
There is at least one path between 1 and n.
"""

"""
My solution: find the connected nodes then find the shortest road

Using DFS, the program can find all the nodes that are connected to node 1
- as the problem constraints guarantees at least 1 path between 1 and n, it is not necessary to check
if node 1 is connected to node n

After finding all the nodes connected to node 1, find the shortest edge connected to any of the connected
nodes.
- As the edges are bi-directional, it is not necessary to check if both nodes are connected to node 1
- As all nodes and edges can be traversed multiple times, any edge connected to the connected nodes is
a candidate for the minimum score.

Runtime: O(N + M) where N is the number of nodes and M is the number of edges in the graph
Space: O(M)
"""


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        traversed = [False for i in range(n + 1)]

        roadDict = {}

        for road in roads:
            if road[0] not in roadDict:
                roadDict[road[0]] = []
            if road[1] not in roadDict:
                roadDict[road[1]] = []
            roadDict[road[0]].append(road[1])
            roadDict[road[1]].append(road[0])

        def dfs(city):
            if traversed[city]:
                return
            traversed[city] = True

            for nextCity in roadDict[city]:
                dfs(nextCity)

        dfs(1)

        minScore = float('inf')
        for road in roads:
            if traversed[road[0]]:
                minScore = min(minScore, road[2])
        return minScore
