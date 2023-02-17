# leetcode problem # 783. Minimum Distance Between BST Nodes

"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.


Example 1:
https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 10^5
"""

"""
My solution: DFS

The minimum distance between a node and its descendents in a BST is always:
1. the difference between the node and the right most descendent of the left subtree, or
2. the difference between the node and the left most descendent of the right subtree
* The two descendent of the largest of the left subtree and the smallest of the right subtree

Using DFS, the tree could be traversed and the recursive return values could be compared
to the value of each node.


Runtime: O(N) where N is the number of nodes in the BST
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def dfs(node, ans=1000000):
            if node.left == node.right == None:
                return [node.val, node.val, ans]
            if node.left == None:
                rightRange = dfs(node.right)
                ans = min(ans, rightRange[0] - node.val, rightRange[2])
                return [node.val, rightRange[1], ans]
            elif node.right == None:
                leftRange = dfs(node.left, ans)
                ans = min(ans, node.val - leftRange[1], leftRange[2])
                return [leftRange[0], node.val, ans]
            else:
                leftRange = dfs(node.left)
                rightRange = dfs(node.right)
                ans = min(
                    ans, node.val - leftRange[1], rightRange[0] - node.val, leftRange[2], rightRange[2])
                return [leftRange[0], rightRange[1], ans]

        ans = dfs(root)[2]

        return ans
