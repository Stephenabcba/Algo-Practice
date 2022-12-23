# leetcode problem # 834. Sum of Distances in Tree

"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.


Example 1:
https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:
https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg
Input: n = 1, edges = []
Output: [0]

Example 3:
https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg
Input: n = 2, edges = [[1,0]]
Output: [1,1]


Constraints:
1 <= n <= 3 * 10^4
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""


"""
Solution by Leetcode Solution

Observation: The tree can be rearranged such that any node can be the root of the tree

Intuition: For every node X, the tree can be broken down into a tree X
with x and all subnodes of x, and a tree Y where y is the parent node of x and
contains all other nodes in the original tree
The total path for each node can be calculated as x@X + y@Y + #(Y), where
x@X is the path length of all nodes in X to reach x, all nodes in Y to
reach y, and #(Y) is the number of nodes in Y
ans[x] - ans[y] = #(Y) - #(X)

Algorithm:
- Definitions:
    - S_node is the subtree with node and all descendants
    - count[node] is the number of nodes in S_node
    - stsum[node] is the sum of distances from node to all nodes in S_node
- Using Postorder traversal to find count and stsum
- ans[root] is stsum[root] after the step above
- Use preorder traversal to find the proper path sum for every node


Runtime: O(N) for number of nodes in the tree
Space: O(N)
"""


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
