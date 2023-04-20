# leetcode problem # 662. Maximum Width of Binary Tree

"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


Example 1:
https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
https://assets.leetcode.com/uploads/2022/03/14/maximum-width-of-binary-tree-v3.jpg
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).

Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""

"""
My solution: DFS

Observation:
In 0-index space, the Nth parent from the left would have their children be
2N and 2N + 1 from the left in the level below
-> When traversing, the index of every node can be determined

Intuition:
Find the width of every level, then find the maximum width
- Using the indexing method observed, the index of every node relative to their level can be
calculated and stored
    - only need to store the left-most and right-most index to find the width
- After traversal is complete, find the level with the maximum width and return the value

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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelWidth = [[0, 0]]

        def traverse(node, level, position):
            if node == None:
                return
            if level >= len(levelWidth):
                levelWidth.append([position, position])
            if position > levelWidth[level][1]:
                levelWidth[level][1] = position
            elif position < levelWidth[level][0]:
                levelWidth[level][0] = position

            traverse(node.left, level + 1, 2 * position)
            traverse(node.right, level + 1, 2 * position + 1)

        traverse(root, 0, 0)
        ans = 0
        for level in levelWidth:
            if level[1] - level[0] > ans:
                ans = level[1] - level[0]
        return ans + 1
