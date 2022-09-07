# Leetcode Problem # 606. Construct String from Binary Tree

"""
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.


Example 1:
https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-1000 <= Node.val <= 1000
"""

"""
My solution: Recursive Preorder Traversal

Observation: the output string always follows the pattern of the node value with the descendent values wrapped in parenthesis after
- if the left child is missing, an empty parenthesis must still be added in its place
- if the right child is missing, do not add an empty pathenthesis

As requested by the problem, the nodes are travelled in the preorder pattern (Node, left, right)
The string can then be built following the pattern observed above

Runtime: O(N) where N in the number of nodes in the tree
Space: O(N) where N in the number of nodes in the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(node):
            # node doesn't exist, return empty string
            if (node == None):
                return ""

            # node exists, process normally
            # find the return strings of the children
            leftString = traverse(node.left)
            rightString = traverse(node.right)

            # if node has no children, no trailing parenthesis needed at all.
            if (len(leftString) == len(rightString) == 0):
                return str(node.val)
            # if the node does not have a right child, the second parenthesis is not needed
            elif (len(rightString) == 0):
                return str(node.val) + "(" + leftString + ")"
            # if the node has both children or only has a right child, both parenthesis are needed.
            return str(node.val) + "(" + leftString + ")(" + rightString + ")"

        return traverse(root)
