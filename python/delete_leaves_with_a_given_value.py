# leetcode problem # 1325. Delete Leaves With a Given Value

"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

Example 1:
https://assets.leetcode.com/uploads/2020/01/09/sample_1_1684.png
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:
https://assets.leetcode.com/uploads/2020/01/09/sample_2_1684.png
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:
https://assets.leetcode.com/uploads/2020/01/15/sample_3_1684.png
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

Constraints:
The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000
"""

"""
My solution: Recursive traversal

Using Inorder traversal, the nodes can be deleted recursively until no
leaf nodes with the target value exists in the tree

Logic:
- Check if the node is a leaf node
    - if the node has children, recursively process the children first
        - replace the children by the returned value
            - the returned value is either the child node itself (no change) or
            None (remove the child node)
        - if the child node is removed, the parent node is considered to have no child
        in that location
    - if either child node exists after recursion, the current node is not a leaf node
    - if the node has no child nodes after recursion, the current node is a leaf node
- If the node is a leaf node with the target value, return None
- Otherwise, return the node itself

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
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def traverse(node):
            isLeaf = True

            if node.left:
                node.left = traverse(node.left)
                if node.left:
                    isLeaf = False
            if node.right:
                node.right = traverse(node.right)
                if node.right:
                    isLeaf = False

            if isLeaf and node.val == target:
                return None
            return node

        return traverse(root)
