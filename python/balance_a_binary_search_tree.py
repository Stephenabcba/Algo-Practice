# leetcode problem # 1382. Balance a Binary Search Tree

"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:
https://assets.leetcode.com/uploads/2021/08/10/balance1-tree.jpg
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:
https://assets.leetcode.com/uploads/2021/08/10/balanced2-tree.jpg
Input: root = [2,1,3]
Output: [2,1,3]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 10^5
"""

"""
My solution: Convert to list then balance

Idea: Using Inorder (left, node, right) traversal, convert the BST into a sorted list (stored separately)
- Using the list, a balanced BST can be reconstructed by splitting the list in half and creating subtrees using each half

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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodesList = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            nodesList.append(node.val)
            if node.right:
                traverse(node.right)

        traverse(root)

        def reconstruct(left, right):
            if left >= right:
                return None
            mid = (left + right) // 2
            midNode = TreeNode(nodesList[mid])
            midNode.left = reconstruct(left, mid)
            midNode.right = reconstruct(mid + 1, right)
            return midNode

        return reconstruct(0, len(nodesList))


"""
Solution by leetcode: Day-Stout-Warren Algorithm / In-Place Balancing

Idea: Convert the tree into a vine (a structure resembling an SLL), then balance it in-place

Runtime: O(N)
Space: O(N)
"""


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Step 1: Create the backbone (vine)
        # Temporary dummy node
        vine_head = TreeNode(0)
        vine_head.right = root
        current = vine_head
        while current.right:
            if current.right.left:
                self.right_rotate(current, current.right)
            else:
                current = current.right

        # Step 2: Count the nodes
        node_count = 0
        current = vine_head.right
        while current:
            node_count += 1
            current = current.right

        # Step 3: Create a balanced BST
        m = 2 ** math.floor(math.log2(node_count + 1)) - 1
        self.make_rotations(vine_head, node_count - m)
        while m > 1:
            m //= 2
            self.make_rotations(vine_head, m)

        balanced_root = vine_head.right
        # Delete the temporary dummy node
        vine_head = None
        return balanced_root

    # Function to perform a right rotation
    def right_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        parent.right = tmp

    # Function to perform a left rotation
    def left_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        parent.right = tmp

    # Function to perform a series of left rotations to balance the vine
    def make_rotations(self, vine_head: TreeNode, count: int):
        current = vine_head
        for _ in range(count):
            tmp = current.right
            self.left_rotate(current, tmp)
            current = current.right
