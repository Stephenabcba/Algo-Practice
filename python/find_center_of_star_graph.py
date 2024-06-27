# leetcode problem # 1791. Find Center of Star Graph

"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Example 1:
https://assets.leetcode.com/uploads/2021/02/24/star_graph.png
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

Constraints:
3 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
"""

"""
My solution: Check the first 2 edges

As all other nodes are connected to the center node, the first two edges must both contain the center node.
-> If the first node in the first edge exists in the second edge, the center node is the first node
    - otherwise, the center node is the second node

Runtime: O(1), runtime does not depend on input
Space: O(1)
"""


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center = edges[0][0]

        if center in edges[1]:
            return center
        else:
            return edges[0][1]
