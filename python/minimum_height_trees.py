# leetcode problem # 310. Minimum Height Trees

"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:
https://assets.leetcode.com/uploads/2020/09/01/e1.jpg
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:
https://assets.leetcode.com/uploads/2020/09/01/e2.jpg
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Constraints:
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""

"""
My solution: DFS and check the tallest 2 children

Observations:
1. When shifting the root from node A to a child node B, node A becomes a child node of B
    - if node A has no other children, the height of subtree of A is 0
    - if node A has other children, and the tallest child was C, then the height of
        subtree of A is the (height of subtree of C) + 1
2. At the minimum height, the tallest 2 children of the root must have a maximum height difference of 1
    - if the tree consists of 1 node, then there are no children
    - if the root only has 1 child, and the child's subtree height is more than 1, then the tree organization
        is not a minimum height tree
    - if the tallest 2 children have the same height, the root is the only minimum height tree
    - if the tallest 2 children have a height difference of 1, the root and the tallest child are both minimum height
    trees
    * There are at least 1 minimum height tree, and at most 2 minimum height trees

Logic:
1. Convert the list of edges into a dictionary for easier access
2. Use DFS to traverse one of the trees and find the height of each subtree
    - While traversing, keep track of the tallest 2 children of each node
    - The initial node to start DFS can be any node, but node 0 is chosen for simplicity
3. Check if node 0 fits the criterion for minimum height tree, as described in observation 2 above
    - if node 0 fits the criterion, then add it to the list
        - add the tallest child, if applicable
    - if node 0 doesn't fit the criterion, check if the tallest child fits the criterion
        - repeat until the minimum height tree is found
        - add node 0 (or the parent node) to the list of tallest children of the new root
4. Return the minum height tree(s) found

Runtime: O(N) where N is the number of nodes in the tree
Space: O(N)
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edgeDict = defaultdict(list)
        for node1, node2 in edges:
            edgeDict[node1].append(node2)
            edgeDict[node2].append(node1)

        longestChildren = [[] for _ in range(n)]

        def dfs(node, parent):
            for edge in edgeDict[node]:
                if parent >= 0 and edge == parent:
                    continue
                edgeHeight = dfs(edge, node) + 1
                if len(longestChildren[node]) < 2:
                    longestChildren[node].append((edgeHeight, edge))
                else:
                    longestChildren[node].append((edgeHeight, edge))
                    longestChildren[node].sort(reverse=True)
                    longestChildren[node].pop()
            while len(longestChildren[node]) < 2:
                longestChildren[node].append((0, -1))
            longestChildren[node].sort(reverse=True)
            return longestChildren[node][0][0] if len(longestChildren[node]) > 0 else 0

        dfs(0, -1)
        cur = 0
        ans = []

        while longestChildren[cur][0][0] - longestChildren[cur][1][0] > 1:
            prev = cur
            cur = longestChildren[cur][0][1]
            longestChildren[cur].append(
                (longestChildren[prev][1][0] + 1, prev))
            longestChildren[cur].sort(reverse=True)

        ans.append(cur)
        if longestChildren[cur][0][0] - longestChildren[cur][1][0] == 1:
            ans.append(longestChildren[cur][0][1])

        return ans
