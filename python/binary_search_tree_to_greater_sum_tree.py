# leetcode problem # 1038. Binary Search Tree to Greater Sum Tree

"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
https://assets.leetcode.com/uploads/2019/05/02/tree.png
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Constraints:
The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.

Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
"""

"""
My solution: Right-Node-Left Traversal

Key variable: Carry
- Used for when the node is a left child
- the right child in a GST would also include the carry of its parent

Recursion logic:
Base Case: The node is a leaf node; increment by the carry and return the 
Recursive Case: The node has children
1. If the node has a right child, pass Carry and process the right child first
    - The node is incremented by the updated value of its right child
    - otherwise, increment by the carry only
2. If the node has a left child, pass the updated node value as the carry to process the left child
3. Return value
    - if the node has a left child, return the updated left child value
    - Otherwise, return the updated node value instead

Runtime: O(N) where N is the number of nodes in the BST
Space: O(N)
- the space complexity includes stack space used during recursion
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(node, carry):

            if node.right:
                node.val += traverse(node.right, carry)
            else:
                node.val += carry

            leftVal = node.val

            if node.left:
                leftVal = traverse(node.left, node.val)

            return leftVal

        traverse(root, 0)

        return root
