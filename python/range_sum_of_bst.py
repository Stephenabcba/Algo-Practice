# leetcode problem # 938. Range Sum of BST

"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.
"""

"""
My solution: BFS for the range

Using a queue, a BFS can be conducted on the BST for all values in the range

Cases:
1. Node value between low and high (inclusive)
- add the node value to the sum
* If node value equals the low boundary, it is only possible for its right child to be in the range
    - As all node values are unique according to the constraints, all left descendents of the node must be smaller than the node
    - the opposite is true if node value equals high boundary
- Except for the exception above, both children of the node are added to the queue

2. Node value below low
- it is only possible for the node's right descendents to be in the range
-> if the node has a right child, add it to the queue
3. Node value above high
- it is only possible for the node's left descendents to be in the range
-> if the node has a left child, add it to the queue

Runtime: O(N) where N is the number of nodes in the BST
Space: O(N) where N is the number of nodes in the BST
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = []
        queueIdx = 0
        queue.append(root)
        total = 0

        while queueIdx < len(queue):
            curNode = queue[queueIdx]
            queueIdx += 1
            if low <= curNode.val <= high:
                total += curNode.val
                if curNode.val == low and curNode.right:
                    queue.append(curNode.right)
                    continue
                if curNode.val == high and curNode.left:
                    queue.append(curNode.left)
                    continue
                if curNode.right:
                    queue.append(curNode.right)
                if curNode.left:
                    queue.append(curNode.left)
            elif curNode.val < low:
                if curNode.right:
                    queue.append(curNode.right)
            elif curNode.val > high:
                if curNode.left:
                    queue.append(curNode.left)

        return total
