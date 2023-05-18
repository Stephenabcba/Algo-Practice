# leetcode problem # 1557. Minimum Number of Vertices to Reach All Nodes

"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.


Example 1:
https://assets.leetcode.com/uploads/2020/07/07/untitled22.png
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

Example 2:
https://assets.leetcode.com/uploads/2020/07/07/untitled.png
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.


Constraints:
2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.
"""

"""
My solution: BFS

By performing BFS, all the nodes will be traversed.
BFS may be initiated multiple times to reach all nodes.
Whenever BFS starts on a node, add the node to the answer.
If BFS reaches a node that is in answer, remove it from answer

The nodes remaining in answer at the end are the minium nodes

Runtime: O(N + E) where N is the number of nodes and E is the number of edges
Space: O(N + E)
"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        startNodes = set()

        edgeDict = {}
        for edgeStart, edgeEnd in edges:
            edgeDict[edgeStart] = edgeDict.get(edgeStart, [])
            edgeDict[edgeStart].append(edgeEnd)

        def bfs(idx):
            queue = [idx]
            queueIdx = 0
            while queueIdx < len(queue):
                if queue[queueIdx] in edgeDict:
                    for node in edgeDict[queue[queueIdx]]:
                        if not visited[node]:
                            queue.append(node)
                            visited[node] = True
                        elif node in startNodes:
                            startNodes.remove(node)
                queueIdx += 1

        visited = [False for _ in range(n)]

        for idx in range(n):
            if not visited[idx]:
                startNodes.add(idx)
                visited[idx] = True
                bfs(idx)

        return list(startNodes)


"""
Solution by leetcode: Check incoming edges

Intuition: If a node has an edge leading to it, the node shouldn't be a starting node.
-> check all edges and eliminate nodes that have edges leading to it
    - at the end, any node without an incoming edge is a starting node.

Runtime: O(N + E) where N is the number of nodes and E is the number of edges
Space: O(N)
"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hasIncomingEdge = [False for _ in range(n)]

        for edge in edges:
            hasIncomingEdge[edge[1]] = True

        ans = []

        for idx in range(n):
            if not hasIncomingEdge[idx]:
                ans.append(idx)

        return ans
