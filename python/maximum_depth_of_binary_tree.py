# leetcode problem # 104. Maximum Depth of Binary Tree

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""

"""
My solution: BFS

BFS will traverse through every node ensuring the deepest depth is reached.

Keep track of the depth of each node, if the current depth is higher than the recorded highest
depth, update highest depth

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth = 0
        queue = [(root, 1)]
        queueIdx = 0
        while len(queue) > queueIdx:
            curNode, curDepth = queue[queueIdx]
            queueIdx += 1
            depth = max(depth, curDepth)
            if curNode.left:
                queue.append((curNode.left, curDepth + 1))
            if curNode.right:
                queue.append((curNode.right, curDepth + 1))

        return depth
