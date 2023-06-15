# leetcode problem # 1161. Maximum Level Sum of a Binary Tree

"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
https://assets.leetcode.com/uploads/2019/05/03/capture.JPG
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
"""

"""
My solution: BFS

Using BFS, the nodes in the tree are processed top->bottom left-> right, where nodes of the same
level are grouped together.

Find the sum for each level and keep track of the highest sum and the level that sum is located
-> if there's two levels with the same sum, keep the lower level

Runtime: O(N) where N is the number of nodes in the binary tree
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        highestSum = -1e6
        level = 1

        queue = [(root, 1)]
        queueIdx = 0
        curSum = 0
        curLevel = 1

        while queueIdx < len(queue):
            if curLevel != queue[queueIdx][1]:
                if curSum > highestSum:
                    highestSum = curSum
                    level = curLevel
                curLevel = queue[queueIdx][1]
                curSum = 0
            curSum += queue[queueIdx][0].val
            if queue[queueIdx][0].left:
                queue.append((queue[queueIdx][0].left, queue[queueIdx][1] + 1))
            if queue[queueIdx][0].right:
                queue.append((queue[queueIdx][0].right, queue[queueIdx][1] + 1))
            
            queueIdx += 1

        if curSum > highestSum:
            level = curLevel

        return level