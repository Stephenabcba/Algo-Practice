# leetcode problem # 101. Symmetric Tree

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:
https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""

"""
My solution: Traverse in pairs recursively

Intuition:
As the tree should be mirrored around its center, the left child of a node should equal
the right child of the mirroring node on the other side and vice versa

Using recursion, the algorithm can check if any part of the tree doesn't fit the requirements
of a symmetric tree.

Recursion Logic:
Base cases:
1. the two mirroring nodes both do not exist:
    - if there's nothing to mirror, symmetry is upheld; return True
2. only one node exists, but not the mirroring node
    - the tree is asymmetric; return False
3. the node values are not identical
    - the tree is asymmetric; return False
Recursive case:
- check the outer children pair (left child of left node and right child of right node)
- check the inner children pair (right child of left node and left child of right node)
- if symmetry is broken at any stage, the tree is asymmetric; return False
- otherwise, return True

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(leftNode, rightNode):
            if leftNode == rightNode == None:
                return True
            elif leftNode == None or rightNode == None:
                return False

            if leftNode.val != rightNode.val:
                return False

            outer = traverse(leftNode.left, rightNode.right)
            inner = traverse(leftNode.right, rightNode.left)
            return outer and inner

        return traverse(root.left, root.right)
