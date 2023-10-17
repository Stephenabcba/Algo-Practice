# leetcode problem # 1361. Validate Binary Tree Nodes

"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:
https://assets.leetcode.com/uploads/2019/08/23/1503_ex1.png
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2019/08/23/1503_ex2.png
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:
https://assets.leetcode.com/uploads/2019/08/23/1503_ex3.png
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Constraints:
n == leftChild.length == rightChild.length
1 <= n <= 10^4
-1 <= leftChild[i], rightChild[i] <= n - 1
"""

"""
My solution: Depth-First Search

The binary tree can be viewed as a directed graph, where leftChild and rightChild lists are the one-way
edges connecting the nodes

For a binary tree to be valid:
1. There must be exactly 1 head in the graph
2. There must be no cycles within the graph
3. The can be at most 1 edge pointing to the node
4. A node can only have at most 2 outgoing edges
-> The algorithm must ensure all 4 criteria are correct
    - 4 is already satisfied by the problem setup
        - a node can have at most a left child and a right child

Depth-first search (dfs) can be used to traverse the graph and check for the remaining 3 criteria
- The visited array holds the state of each node, which can be one of three states:
    - -1: the node has not been visited
    - 0: dfs was initiated on the node; the node is a head of a graph
    - 1: dfs has passed through and visited this node
- When performing a dfs, traverse one side of the node as far as possible, then traverse down the other side
    - if any node already has a state of 1 when traversing, the graph has a cycle or 2 incoming edges to a node
        - in both cases, the binary tree is invalid; end recursion and return False
    - if any node already has a state of 0 when traversing, all outgoing edges from the node has been traversed
        - connect the node to the tree (change state of the node to 1), and end recursion
    - if the node has a state of -1, traverse normally.
- As it is unknown which node is the head, all unvisited nodes need to be traversed to find the head
In this logic, if dfs returns false at any given point, the binary tree is invalid; return False

If dfs did not return false, the tree is a valid candidate.
- check whether the node has multiple heads
    - this can be done by counting the number of 0's in the visited array at the end
    - if the node has a single head, the tree is valid; return True
    - otherwise, return False

Runtime: O(N) where N is the number of nodes in the graph
Space: O(N)
"""

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [-1 for _ in range(n)]

        def dfs(node):
            if visited[node] == 0:
                visited[node] = 1
                return True
            if visited[node] == 1:
                return False
            visited[node] = 1
            res = True
            if leftChild[node] >= 0:
                res = res and dfs(leftChild[node])
            if res and rightChild[node] >= 0:
                res = res and dfs(rightChild[node])
            return res

        for node in range(n):
            if visited[node] < 0:
                res = dfs(node)
                if not res:
                    return False
                visited[node] = 0
        
        headCount = 0
        for node in visited:
            if node == 0:
                headCount += 1

        return headCount == 1