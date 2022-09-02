# leetcode problem # 1448. Count Good Nodes in Binary Tree

"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


Example 1:
https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""


"""
My solution: traverse every node 
While traversing the nodes recursively, keep track of the highest value encountered so far.
- If a node is greater than or equal to the highest value encountered, add 1 to the answer count
    - if needed, update the highest value encountered to the current value

Base Case: Node is null, stop recursing
Recursive Case: Node exists, process the node and its children

Runtime: O(N) where N is the number of nodes in the tree
Space: O(1), memory useage does not depend on input size
* recursion memory useage is not counted
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, limit):
            if node == None:
                return 0
            validNode = 0
            if node.val >= limit:
                validNode = 1
            limit = max(node.val, limit)
            return validNode + traverse(node.left,limit) + traverse(node.right,limit)

        return traverse(root,-1000000)