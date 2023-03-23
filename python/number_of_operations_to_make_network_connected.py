# leetcode problem # 1319. Number of Operations to Make Network Connected

"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.


Example 1:
https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:
https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Constraints:
1 <= n <= 10^5
1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
"""

"""
My solution: DFS

Intuition: Find the connected components and connect them
- a component can be either be 1 computer or a cluster of computers connected with each other
- components are not connected to other components
- it takes count(components) - 1 connections to connect all the components
* there must be at least n - 1 connections to connect all the computers.

Using DFS, the connected components can be found
- DFS may need to be initiated on multiple nodes to find all the connected components

A dictionary can be used to access all connections to a node in constant time.

Runtime: O(N + M) where N is the number of computers and M is the number of connections
Space: O(N)
"""


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cableCount = len(connections)
        if cableCount < n - 1:
            return -1

        connectionDict = {}

        for connection in connections:
            connectionDict[connection[0]] = connectionDict.get(
                connection[0], [])
            connectionDict[connection[0]].append(connection[1])
            connectionDict[connection[1]] = connectionDict.get(
                connection[1], [])
            connectionDict[connection[1]].append(connection[0])

        visited = [False for i in range(n)]

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            if node in connectionDict:
                for computer in connectionDict[node]:
                    dfs(computer)

        componentCount = 0

        for node in range(n):
            if visited[node]:
                continue
            inNetwork = dfs(node)

            componentCount += 1

        return componentCount - 1
