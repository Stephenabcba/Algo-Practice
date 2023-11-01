# leetcode problem # 501. Find Mode in Binary Search Tree

"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""


"""
My solution: Count with dictionary

Logic:
1. find the count of each value in the tree
2. Sort the count
3. Keep the values with the highest counts
4. Return the values

Runtime: O(N + M * logM) where N is the number of nodes in the bst, and M is the number of unique values within the tree
Space: O(M)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodeCounts = defaultdict(int)

        def traverse(node):
            nodeCounts[node.val] += 1
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)

        counts = []
        for node in nodeCounts:
            counts.append([nodeCounts[node], node])

        counts.sort(reverse=True)

        while counts[-1][0] < counts[0][0]:
            counts.pop()

        return [node[1] for node in counts]