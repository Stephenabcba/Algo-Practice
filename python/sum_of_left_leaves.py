# leetcode problem # 404. Sum of Left Leaves

"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""

"""
My solution: Recursion

Base Case: Node is a leaf node (no children)
- if it is a left child, return the node's value, otherwise return 0
Recursive Case: The node has children
-Traverse to the children that exist, and return the sum of the values returned

The recursive function has an extra input to flag whether it was called as a left child
of another node

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(node, isLeft):
            curSum = 0
            if node.left == node.right == None:
                return node.val if isLeft else 0
            if node.left:
                curSum += traverse(node.left, True)
            if node.right:
                curSum += traverse(node.right, False)
            return curSum

        return traverse(root, False)
