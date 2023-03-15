# leetcode problem # 958. Check Completeness of a Binary Tree

"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:
The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
"""

"""
My solution: Recursive Traversal

Observation:
1. In a complete binary tree, the left most descendent must have the highest depth
    - if any other node has a higher depth, the nodes are not as far left as possible
2. All nodes with depth lower than the maximum depth must not be null

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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        allowedDepth = 1
        cur = root
        while cur.left:
            allowedDepth += 1
            cur = cur.left

        minDepth = allowedDepth - 1

        def traverse(node, level, depths):
            if node == None:
                if level <= depths[1]:
                    return -1
                return 0
            if level > depths[0]:
                return -1
            left = traverse(node.left, level + 1, depths)
            if left == -1:
                return -1
            if left == 0 and level < depths[0]:
                depths[0] -= 1
            right = traverse(node.right, level + 1, depths)
            if right == -1:
                return -1
            if right == 0 and level < depths[0]:
                depths[0] -= 1
            return 1

        ans = traverse(root, 1, [allowedDepth, minDepth])
        print(ans)

        return ans == 1
