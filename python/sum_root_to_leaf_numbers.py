# leetcode problem # 129. Sum Root to Leaf Numbers

"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.


Example 1:
https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""

"""
My solution: Recursive traversal

Uusing recursive traversal, the parent node will recursively call the function to process
its children nodes, forming a chain of recursive functions from root to each leaf node

Construct the number when traversing from root to leaf, multiplying the current value by 10 every recursion.

Recursion logic:
Base Case: Node doesn't exist
- if a node doesn't exist, no number is formed, return -1
Recursive Case: process the children
- There are 3 main outcomes of recursion:
    1. Both children do not exist (both recursion returns -1)
        - the parent node is a leaf node, return the constructed number
    2. One of the children do not exist (one recursion returns -1)
        - the other child branch is the only branch with constructed numbers
            - return the child's return value
    3. Both children exists
        - return the sum of both children's return values

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def calcSum(node, parentVal):
            if node == None:
                return -1
            curVal = parentVal * 10 + node.val
            left = calcSum(node.left, curVal)
            right = calcSum(node.right, curVal)

            if left == right == -1:
                return curVal
            if left == -1:
                return right
            if right == -1:
                return left
            return left + right

        return calcSum(root, 0)
