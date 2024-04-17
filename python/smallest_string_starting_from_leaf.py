# leetcode problem # 988. Smallest String Starting From Leaf

"""
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example 1:
https://assets.leetcode.com/uploads/2019/01/30/tree1.png
Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
https://assets.leetcode.com/uploads/2019/01/30/tree2.png
Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
https://assets.leetcode.com/uploads/2019/02/01/tree3.png
Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"

Constraints:
The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
"""

"""
My solution: Keep a stack of current letters and compare at leaf nodes

When traversing to a node, add the node to the current set of nodes
When returning to the parent, remove the node from the set

Base Case: the current node is a leaf node
- compare the current set of letters against the best set of letters
- if the current set is better, set it as the best set
Recursive Case: the current node has children
- traverse to all existing children

Runtime: O(N * logN) where N is the number of nodes in the tree
Space: O(logN)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = [100]

        def traverse(node, cur):
            cur.append(node.val)
            if node.left == node.right == None:
                idx = 1
                curIsSmallest = 0
                while idx - 1 < len(cur) and idx - 1 < len(smallest):
                    if cur[-idx] < smallest[-idx]:
                        curIsSmallest = 1
                        break
                    elif cur[-idx] > smallest[-idx]:
                        curIsSmallest = -1
                        break
                    idx += 1
                if curIsSmallest == 1 or curIsSmallest == 0 and len(cur) < len(smallest):
                    smallest.clear()
                    for val in cur:
                        smallest.append(val)
            else:
                if node.left:
                    traverse(node.left, cur)
                if node.right:
                    traverse(node.right, cur)

            cur.pop()

        traverse(root, [])
        smallest.reverse()
        return "".join([chr(letter + ord("a")) for letter in smallest])
