# leetcode problem # 515. Find Largest Value in Each Tree Row

"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""

"""
My solution: Traverse to each node and compare values

Idea: Compare the value of each node to the highest value recorded for the row the row
- if the value of the node is higher, update the highest value of the row
- if there's no highest value of the row recorded yet, the node's value is added to the record

When traversing, keep track of the row number the node is on.
The traversal methoed used is preorder (node, left, right).

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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(node, row, ans):
            if node:
                if row >= len(ans):
                    ans.append(node.val)
                elif ans[row] < node.val:
                    ans[row] = node.val

                traverse(node.left, row + 1, ans)
                traverse(node.right, row + 1, ans)

        traverse(root, 0, ans)

        return ans