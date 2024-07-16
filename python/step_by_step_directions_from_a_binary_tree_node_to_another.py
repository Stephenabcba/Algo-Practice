# leetcode problem # 2096. Step-By-Step Directions From a Binary Tree Node to Another

"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:
https://assets.leetcode.com/uploads/2021/11/15/eg1.png
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:
https://assets.leetcode.com/uploads/2021/11/15/eg2.png
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""

"""
My solution: Find path to each then combine

Idea: Find the path to each node, then combine the two paths
- if the two paths share common parents, the path from start to dest can skip those nodes

Logic:
1. Find the path from root to start and root to dest
- DFS is used here, and the path is saved as list
2. Find the common parents of the nodes
- the common parents are the first X nodes that are identical for both paths
- the common parents are skipped
3. Create the path from start to dest
- retrace the path from start to the common ancestor
    - each step adds an "U" to go up to its parent
- follow the path down from the ancestor to dest
    - each step is exactly as saved in the path to dest, no change needed
4. Return the path

Runtime: O(N) where N is the number of nodes in the tree
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pathToStart = []
        pathToDest = []

        def findNode(curNode, value, path):
            if curNode.val == value:
                return True

            if curNode.left:
                path.append("L")
                if findNode(curNode.left, value, path):
                    return True
                path.pop()
            if curNode.right:
                path.append("R")
                if findNode(curNode.right, value, path):
                    return True
                path.pop()
            return False

        findNode(root, startValue, pathToStart)
        findNode(root, destValue, pathToDest)

        finalPath = []
        skip = 0
        while skip < len(pathToStart) and skip < len(pathToDest) and pathToStart[skip] == pathToDest[skip]:
            skip += 1
        for idx in range(skip, len(pathToStart)):
            finalPath.append("U")
        finalPath += pathToDest[skip:]

        return "".join(finalPath)
