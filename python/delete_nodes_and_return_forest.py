# leetcode problem # 1110. Delete Nodes And Return Forest

"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:
https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

Constraints:
The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""

"""
My Solution: BFS

By converting the list of nodes to delete to a set, the values can be accessed in constant time

Using a queue, the program can sequentially process every node in the tree
- starting from the root, add any children it has to the queue
- if the parent is deleted, the node is a root of a tree in the forest
    - add the node to the answer
    - in the queue, also save whether the parent of the node is deleted

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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleteSet = set(to_delete)

        q = deque()
        q.append([root, True])

        ans = []

        while len(q) > 0:
            node, isNewRoot = q.popleft()
            delCurNode = False
            if node.val in deleteSet:
                delCurNode = True
            if node.left:
                q.append([node.left, delCurNode])
                if node.left.val in deleteSet:
                    node.left = None
            if node.right:
                q.append([node.right, delCurNode])
                if node.right.val in deleteSet:
                    node.right = None

            if isNewRoot and not delCurNode:
                ans.append(node)

        return ans
