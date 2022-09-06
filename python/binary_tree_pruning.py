# Leetcode problem # 814. Binary Tree Pruning

"""
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.


Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Constraints:
The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
"""

"""
My solution: Traverse the tree
The traversal logic determines whether the subtree contains 1
- if any left or right child's subtree does not contain 1, remove the subtree from the tree
    - in the current logic, the nodes are removed one by one.

In order to handle the edge case of the root also being removed (if the entire tree does not contain 1),
a dummy tree node is created as the parent of the root
    - this way, the root is a child and can be removed if needed
    - if the root is removed, an empty tree is returned

Runtime: O(N) where N is the number of nodes in the tree
Space: O(1), no scaling space useage is needed except for recursion.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node):
            # Base case: node is empty, the subtree cannot contain 1
            if (node == None):
                return False

            containsOne = False

            # If the current node is 1, then the current node will never be deleted
            if (node.val == 1):
                containsOne = True

            # If the left subtree contains 1, then the current node will nto be deleted
            # If the left subtree doesn't contain 1, then remove the left node
            if (traverse(node.left)):
                containsOne = True
            else:
                node.left = None

            #  Repeate the logic above with the right node
            if (traverse(node.right)):
                containsOne = True
            else:
                node.right = None

            return containsOne

        # create a dummy node so the root can be removed if needed.
        dummy = TreeNode()
        dummy.left = root
        traverse(dummy)
        return dummy.left
