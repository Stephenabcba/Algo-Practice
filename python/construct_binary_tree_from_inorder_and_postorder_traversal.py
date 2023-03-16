# leetcode problem # 106. Construct Binary Tree from Inorder and Postorder Traversal

"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


Example 1:
https://assets.leetcode.com/uploads/2021/02/19/tree.jpg
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""

"""
My Solution: Recursion

Observation:
1. Inorder traversal is always in the format (left subtree, root, right subtree)
2. Postorder traversal is always in the format (left subtree, right subtree, root)
* This pattern is preserved even in the subtrees

Logic: break the tree down into subtrees
1. the root of the subtree is always the last node in the postorder format
2. using the root, the inorder traversal can be easily split into left and right subtrees
3. however, the cutoff point of the left and right subtree in postorder traversal is unclear
    - using binary search, the algorithm can check for the cutoff point
        - whether a node is in the left or right subtree can be confirmed using the inorder traversal
4. after the subtrees have been separated, repeat steps 1-3 on each subtree until the binary tree is
reconstructed.

Runtime: O(N * logN) where N is the number of nodes in the binary tree
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}
        postorderIndex = {}
        for idx in range(len(inorder)):
            inorderIndex[inorder[idx]] = idx
            postorderIndex[postorder[idx]] = idx

        def construct(postorderStart, postorderEnd, inorderStart, inorderEnd):
            if postorderStart > postorderEnd or inorderStart > inorderEnd:
                return None
            node = TreeNode(postorder[postorderEnd])
            inorderCenterIdx = inorderIndex[postorder[postorderEnd]]
            if inorderCenterIdx - 1 >= inorderStart and inorderCenterIdx + 1 <= inorderEnd:
                low = postorderStart
                high = postorderEnd
                while low < high:
                    mid = (low + high) // 2
                    if inorderIndex[postorder[mid]] > inorderCenterIdx:
                        high = mid
                    else:
                        low = mid + 1
                node.left = construct(
                    postorderStart, high - 1, inorderStart, inorderCenterIdx - 1)
                node.right = construct(
                    high, postorderEnd - 1, inorderCenterIdx + 1, inorderEnd)
            elif inorderCenterIdx - 1 < inorderStart:
                node.right = construct(
                    postorderStart, postorderEnd - 1, inorderCenterIdx + 1, inorderEnd)
            else:
                node.left = construct(
                    postorderStart, postorderEnd - 1, inorderStart, inorderCenterIdx - 1)

            return node

        return construct(0, len(postorder) - 1, 0, len(postorder) - 1)
