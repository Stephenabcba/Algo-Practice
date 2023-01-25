# leetcode problem # 2359. Find Closest Node to Given Two Nodes

"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

 

Example 1:


Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:


Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
 

Constraints:

n == edges.length
2 <= n <= 10^5
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
"""

"""
My solution: Graph Traversal

Intuition:
- Traverse the graph and find the distance from the target nodes to any reachable node
    - if a node is unreachable, it is set as infinite distance from the node in this logic
- Check each node to find the minimum maximum distance from the target nodes to the node
    - ex. if it takes 5 steps from node1 to node#5 and 10 steps from node2 to node#5, the
    maximum distance is 10.
        - the minimum of that maximum value is wanted.
    - keep track of the index of the minimum maximum value
- Return the index found in the previous step

Graph traversal can be done with a modified version of iterative BFS
- as there is at most 1 outgoing edge for any node, the queue will only have at most 1
item at any given time
    -> just need to keep the index of the next node, no need to keep track of a whole
    queue
- if cycles exist, traversal is done
    - as there's only one outgoing edge for each node, the existence of a cycle means
    that no new nodes can be found
    - if the current node has a distance less than infinity, it has been traversed
    before, meaning that the cycle has been completed

Slight optimization: If the other target node is reached while traversing the current
target node, there's no need to continue iterating
- the closest node is the other target node

Runtime: O(N) where N is the number of nodes in the graph
Space: O(N)
"""


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def traverse(startNode, otherNode):
            distances = [float('inf') for _ in edges]
            nextNode = startNode
            steps = 0
            while nextNode != -1 and distances[nextNode] == float('inf'):
                distances[nextNode] = steps
                if nextNode == otherNode:
                    break
                steps += 1
                nextNode = edges[nextNode]
            return distances

        node1Distances = traverse(node1, node2)
        node2Distances = traverse(node2, node1)

        smallestIdx = -1
        distance = float('inf')
        for idx in range(len(edges)):
            larger = max(node1Distances[idx], node2Distances[idx])
            if larger < distance:
                smallestIdx = idx
                distance = larger

        return smallestIdx
