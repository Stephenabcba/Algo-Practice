# leetcode problem # 530. Minimum Absolute Difference in BST

"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10^4].
0 <= Node.val <= 10^5
"""

"""
My solution: postorder traversal

- compare the rightmost descendent of the left side and the leftmost descendent of the 
right side to the current node

Runtime: O(N) where N is the number of nodes that are in the tree
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            leftData = [1000000, node.val, node.val]
            rightData = [1000000, node.val, node.val]
            hasLeft = False
            hasRight = False

            if node.left:
                leftData = traverse(node.left)
                hasLeft = True

            if node.right:
                rightData = traverse(node.right)
                hasRight = True
            
            curMin = min(leftData[0], rightData[0])

            if hasLeft:
                curMin = min(curMin, node.val - leftData[2])
            if hasRight:
                curMin = min(curMin, rightData[1] - node.val)

            return [curMin, leftData[1], rightData[2]]

        return traverse(root)[0]


"""
Solution by leetcode: Inorder traversal

when inorder traversal is performed on a binary search tree, the
values will be traversed from smallest to largest
-> only need to compare every node to the previous node traversed

Compared to my solution, fewer comparisons are done and and less data is
generated in each stack, leading to faster runtime and memory usage

Runtime: O(N) where N is the number of nodes in the BST
Space: O(N)
"""


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDistance = 1e9
        # Initially, it will be null.
        self.prevNode = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            # Find the difference with the previous value if it is there.
            if self.prevNode is not None:
                self.minDistance = min(self.minDistance, node.val - self.prevNode)
            self.prevNode = node.val
            inorder(node.right)

        inorder(root)
        return self.minDistance