# leetcode problem # 785. Is Graph Bipartite?


"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.


Example 1:
https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

Constraints:
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
"""

"""
My solution: DFS

In an undirected graph, DFS will traverse through all connected nodes in the graph
- when traversing, ensure that every edge connects nodes across partitions
    - if a node has not been assigned a partition, assign the node to the opposite partition
        - continue traversing through the node to complete the DFS
    - if a node has been assigned a partition, ensure that the node is in the opposite partition
        - if the connected node is in the same partition, the graph cannot be bipartite
            - return False
        - otherwise, no further action needs to be done

Keep track of which nodes have been traversed, and which partition the node is assigned to
- this can be done with a single list
    - if the value is 0, the node hasn't been traversed
    - if the value is 1, the node is assigned to partition 1
    - if the value is -1, the node is assigned to partition 2

DFS may need to be initiated multiple times to cover the entire graph
- it is arbitrary which side the first node of a DFS traversal starts on

Runtime: O(N + E) where N is the number of nodes and E is the number of edges in the graph
Space: O(N)
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        traversed = [0 for _ in graph]

        def dfs(node):
            for connectedNode in graph[node]:
                if traversed[connectedNode]:
                    if traversed[connectedNode] == traversed[node]:
                        return False
                else:
                    traversed[connectedNode] = -traversed[node]
                    if not dfs(connectedNode):
                        return False
            return True

        for node in range(len(graph)):
            if not traversed[node]:
                traversed[node] = 1
                if not dfs(node):
                    return False

        return True


"""
Unoptimized solution: saving the results in 2 sets

perform DFS while saving nodes connected by edges in opposing sets.

Runtime and Space have the same big-O complexity as the solution above, but uses
extra space to save the node assignments in separate sets
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set1 = set()
        set2 = set()
        traversed = [False for _ in graph]

        def dfs(node, curSet, otherSet):
            curSet.add(node)
            traversed[node] = True
            for connectedNode in graph[node]:
                if connectedNode in curSet:
                    return False
                if not traversed[connectedNode]:
                    if not dfs(connectedNode, otherSet, curSet):
                        return False
            return True

        for node in range(len(graph)):
            if not traversed[node]:
                if not dfs(node, set1, set2):
                    return False

        return True
