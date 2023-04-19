# leetcode problem # 1372. Longest ZigZag Path in a Binary Tree

"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.


Example 1:
https://assets.leetcode.com/uploads/2020/01/22/sample_1_1702.png
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
https://assets.leetcode.com/uploads/2020/01/22/sample_2_1702.png
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0


Constraints:
The number of nodes in the tree is in the range [1, 5 * 10^4].
1 <= Node.val <= 100
"""

"""
My solution: Recursive DFS

Intuition:
When traversing the tree, try to continue the zigzag for the child in the correct direction and start a new zigzag for the 
other child.
- Ex: if the parent node is a right child, the left child would extend the zigzag, and the right child would start a new zigzag
    -> it is known which way the zigzag is continued based on the position of the node relative to the parent node above

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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigzag(node, curLength, toRight):
            if node == None:
                return curLength

            leftLength = 0
            rightLength = 0
            if curLength != -1:
                if toRight:
                    leftLength = curLength + 1
                else:
                    rightLength = curLength + 1
            return max(zigzag(node.left, leftLength, False), zigzag(node.right, rightLength, True))

        return zigzag(root, -1, False)
