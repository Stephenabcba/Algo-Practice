# leetcode problem # 623. Add One Row to Tree

"""
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.


Example 1:
https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:
https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg
Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
The depth of the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
-10^5 <= val <= 10^5
1 <= depth <= the depth of tree + 1
"""

"""
My solution: recursive preorder traversal

Base Cases:
1. The node does not exist, no need to recurse
2. The node is at the parent level of the target depth to add the row of nodes
- create the new nodes with values val
- connect the old left and right nodes to the left and right child of the new nodes, respectively
    - the old left node is the left child of the new left node
    - the old right node is the right child of the new right node
    * note: it is possible to add the new values as leaf nodes, meaning no actual old children exist
        - it's unclear in the instructions, but basically the new nodes should be added to all places where the parent node of the target depth exists
- connect the new nodes to the parent node

Recursive Case:
The node has not reached the parent of the target depth
- continute recursion to the children nodes
- update the current depth accordingly

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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.left = root

        def recurse(node, curDepth):
            if (node is None):
                return -1
            if (curDepth == depth):
                newLeft = TreeNode(val=val)
                newLeft.left = node.left
                node.left = newLeft
                newRight = TreeNode(val=val)
                newRight.right = node.right
                node.right = newRight
                return 0
            recurse(node.left, curDepth + 1)
            recurse(node.right, curDepth + 1)

        recurse(dummy, 1)
        return dummy.left
