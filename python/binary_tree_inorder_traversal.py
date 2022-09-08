# Leetcode problem # 94. Binary Tree Inorder Traversal

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:
https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

"""
My solution: Recursive traversal
Follow the inorder pattern of Left, Node, Right

Runtime: O(N) where N is the number of nodes in the tree
Space: O(N) where N is the number of nodes in the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(node):
            if (node == None):
                return
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)
        traverse(root)
        return ans
