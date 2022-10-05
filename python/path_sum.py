# leetcode problem # 112. Path Sum

"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

"""
My solution: preorder traversal while keeping a subsum

Follow the preorder binary tree traversal (Node, Left, Right)

Keep track of the subtotal of the path while traversing

If a leaf node is encountered, check if the sum of the path equals the target
- if they are equal, return True
-> propogate the True result to the first call
-> if none of the paths have the target sum, return False

Runtime: O(N) where N is the number of nodes in the tree
Space: O(N) where N is the number of nodes in the tree
* this ignores the memory usage of recursion

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node, subTotal):
            if (node is None):
                return None
            subTotal += node.val
            left = traverse(node.left, subTotal)
            right = traverse(node.right, subTotal)
            if (left == True or right == True):
                return True
            if (left == right == None):
                if (subTotal == targetSum):
                    return True
            return False
        return traverse(root, 0)
