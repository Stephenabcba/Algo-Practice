# leetcode problem # 222. Count Complete Tree Nodes

"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia (http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees), every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.


Example 1:
https://assets.leetcode.com/uploads/2021/01/14/complete.jpg
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1

Constraints:

The number of nodes in the tree is in the range [0, 5 * 10^4].
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.
"""

"""
My solution: Binary search the binary tree

As the binary tree is complete, the number of nodes in every level of the tree is know except for the last level.
- the number of nodes is 2 ^ level (where root is the 0th level)
- thus, the total number of nodes (excluding the last level) can be calculated and summed.

The height of the tree can be determined from counting the number of traversals needed to reach the left-most node in the tree.
- this is guaranteed by the complete binary tree

To find the number of nodes in the last level, a binary-search logic is implemented.
- it takes O(logM) passes to complete, where M is the theoretical maximum nodes that the last level can have
- each pass takes O(height) time to traverse and complete, where height is also in logarithmic relation with N  


Runtime: O((log N) ^ 2), where N is the number of nodes in the binary tree
Space: O(1), memory usage should not scale with input size
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        height = 0
        curNode = root
        while (curNode is not None):
            curNode = curNode.left
            height += 1

        if height <= 1:
            return height

        totalNodes = 0
        for level in range(height - 1):
            totalNodes += 2 ** level

        nodesToAdd = 2 ** (height - 2)
        parent = root
        traverseLevel = height - 2

        while nodesToAdd > 0:
            curNode = parent.left
            if curNode is None:
                break

            for traverseCount in range(traverseLevel):
                curNode = curNode.right

            if curNode is not None:
                totalNodes += nodesToAdd
                parent = parent.right
                if parent is not None and nodesToAdd == 1:
                    totalNodes += 1
            else:
                parent = parent.left

            if parent is None:
                break

            nodesToAdd = nodesToAdd // 2
            traverseLevel -= 1

        return totalNodes
