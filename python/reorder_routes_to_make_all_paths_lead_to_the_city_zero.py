# leetcode problem # 1466. Reorder Routes to Make All Paths Lead to the City Zero

"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.


Example 1:
https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
https://assets.leetcode.com/uploads/2020/05/13/sample_2_1819.png
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:

2 <= n <= 5 * 10^4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""

"""
My solution: DFS

Using a dictionary, the roads connected to a city can be accessed in constant time.
- Modifications:
    1. save the roads in both directions
    2. keep track of whether the road is in the given direction
    - ex: if there is a road connecting node 1 to 2, save both 1->2 and 2->1 in
    the dictionary
        - 1->2 is saved with True, meaning that it is in the direction given in connections
        - 2->1 is saved with False.

Perform DFS from node 0
- as the roads are saved in both direction in the dictionary, there is no issue with not finding
a path.
- when traversing in the graph, if a traversed road is saved with True, the road needs to be reversed.
- count the number of roads that need to be reversed.

Runtime: O(N) where N is the input integer N
Space: O(N)
"""


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connectionDict = {}

        for connection in connections:
            if connection[0] not in connectionDict:
                connectionDict[connection[0]] = []
            if connection[1] not in connectionDict:
                connectionDict[connection[1]] = []
            connectionDict[connection[0]].append((connection[1], True))
            connectionDict[connection[1]].append((connection[0], False))

        visited = [False for i in range(n)]

        def dfs(node, isReversed):
            if visited[node]:
                return 0
            visited[node] = True

            reversals = 0
            if isReversed:
                reversals += 1

            for connection in connectionDict[node]:
                reversals += dfs(connection[0], connection[1])
            return reversals

        return dfs(0, False)
