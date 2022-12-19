# leetcode problem # 1971. Find if Path Exists in Graph

"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:
https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:
1 <= n <= 2 * 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""

"""
My Solution: DFS

As the problem is finding paths between two nodes, DFS can be used.

To facitilate finding edges that connect to the node, the edges list is
converted into an edges dictionary

DFS explores the graph and keeps track of the nodes visited. If the
destination node is found, recursion ends. Otherwise, recursion ends
when all reachable nodes have been explored.

Return True if DFS has reached destination node starting from source node,
otherwise return False.

Time: O(N) where N is the number of edges in the graph
Space: O(N) where N is the number of edges in the graph
"""


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False for _ in range(n)]

        edgesDict = {}

        for edge in edges:
            u = edge[0]
            v = edge[1]
            if u not in edgesDict:
                edgesDict[u] = []
            if v not in edgesDict:
                edgesDict[v] = []
            edgesDict[u].append(v)
            edgesDict[v].append(u)

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            if visited[destination]:
                return
            for otherNode in edgesDict[node]:
                dfs(otherNode)

        dfs(source)
        return visited[destination]
