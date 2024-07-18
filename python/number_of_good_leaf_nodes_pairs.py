# leetcode problem # 1530. Number of Good Leaf Nodes Pairs

"""
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:
https://assets.leetcode.com/uploads/2020/07/09/e1.jpg
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:
https://assets.leetcode.com/uploads/2020/07/09/e2.jpg
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Constraints:
The number of nodes in the tree is in the range [1, 2^10].
1 <= Node.val <= 100
1 <= distance <= 10
"""

"""
My solution: DFS

Idea: Use each parent node as a "bridge"
- the bridge is the lowest common ancestor of the good pair
- the sum of distances from either node must not exceed distance
- the parent nodes by definition can never be leaf nodes
    - if a node is a parent node, it has children -> the node cannot be a leaf node

Logic: Use DFS to traverse the tree, and use the concept above to count the good pairs
- keep count of the number of nodes at each distance from the parent node

Runtime: O(N * M ^ 2) where N is the number of nodes, and M is the integer distance
Space: O(N * M)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def traverse(node, leafDistances):
            if not node.left and not node.right:
                leafDistances[0] = 1
                return 0
            leftLeaves = [0] * distance
            rightLeaves = [0] * distance
            goodCount = 0
            if node.left:
                goodCount += traverse(node.left, leftLeaves)
            if node.right:
                goodCount += traverse(node.right, rightLeaves)
            if node.left and node.right:
                for leftLeaf in range(distance):
                    for rightLeaf in range(distance - leftLeaf - 1):
                        goodCount += leftLeaves[leftLeaf] * \
                            rightLeaves[rightLeaf]
            for idx in range(distance - 1):
                leafDistances[idx + 1] += leftLeaves[idx] + rightLeaves[idx]
            return goodCount

        return traverse(root, [0] * distance)
