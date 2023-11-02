# leetcode problem # 2265. Count Nodes Equal to Average of Subtree

"""
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:
The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.

Example 1:
https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example 2:
https://assets.leetcode.com/uploads/2022/03/26/image-20220326133920-1.png
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""

"""
My solution: Recursion

Logic: Find the sum and the number of nodes recursively
- Base case: if a node doesn't exist, stop iterating
    - an empty node does not contribute to the count and sum
- Recursive case: 
    1. find the count and sum of the two children
    2. add the counts (+1 for the current node) and the sums + the current node's value
    3. check if the sum / count (truncated) equals to the node's value
        - if they match, increment the counter

Postorder traversal (left, right, node) is used as the information from the children are needed to process the current node

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
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def traverse(node):
            if node is None:
                return [0, 0]
            left = traverse(node.left)
            right = traverse(node.right)
            total = left[0] + right[0] + node.val
            nodeCount = left[1] + right[1] + 1

            average = total // nodeCount
            if average == node.val:
                self.ans += 1
            return [total, nodeCount]

        traverse(root)

        return self.ans
