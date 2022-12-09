# leetcode problem # 1026. Maximum Difference Between Node and Ancestor

"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.


Example 1:
https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:
https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg
Input: root = [1,null,2,null,0,3]
Output: 3

Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10^5
"""

"""
My solution: Recursive DFS

Using recursive preorder traversal, the recursive functions are able to 
keep track of the minimum and maximum values visited in a path from root
to a leaf node

at every node, the difference is calculated and compared against the differences found
by its descendents, and the largest difference is returned.

Runtime: O(N) where N is the number of nodes in the binary tree
Space: O(N) where N is the number of nodes in the binary tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(node, minVal, maxVal):
            if node is None:
                return 0
            maxVal = max(node.val, maxVal)
            minVal = min(node.val, minVal)
            leftDiff = traverse(node.left, minVal, maxVal)
            rightDiff = traverse(node.right, minVal, maxVal)

            return max(maxVal - minVal, leftDiff, rightDiff)

        return traverse(root, root.val, root.val)
