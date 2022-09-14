# leetcode problem # 1457. Pseudo-Palindromic Paths in a Binary Tree

"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.


Example 1:
https://assets.leetcode.com/uploads/2020/05/06/palindromic_paths_1.png
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
https://assets.leetcode.com/uploads/2020/05/07/palindromic_paths_2.png
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 9
"""

"""
My solution: Recursively traverse the tree and keep track of values in the path

Depth-First Search the tree to look for leaf nodes
- Base case:
1. Node is empty, path does not extend here; return 0
2. Node is a leaf node, path is completed here; check if the path is pseudo-palindromic
    - A leaf node can be checked by confirming both of its children are None.
    - A path can be checked by counting the number of values with odd number occurances
        - if more than 1 value occurs for odd number of times, the path is not pseudo-palindromic
        - otherwise, the path is pseudo-palindromic.
- Recursive case:
Node is not empty, and has at least one child
-> continue recursion on the node's child(ren)

To keep track of the values in a path, a dictionary can be used to keep count.
- This is especially efficient as the problem constraints limit the nodes' values to digits from 1 to 9
- When a node is considered in a path through recursion, increment value of the key in the dictionary corresponding to the node's value
- When a node is removed from a path (before returning to the parent node), decrement value of the key in the dictionary corresponding to the node's value

Runtime: O(N) where N is the number of nodes in the tree
- The checking function is technically a constant-time function, as it only iterates up to 9 times every call.
Space: O(1), The memory usage only scales with input size until a very small limit
- The dictionary will vary in size between 0 to 9, but will not increase in size beyond 9
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        def checkPath(numCounts):
            oddCount = 0
            for num in numCounts.values():
                if num % 2 == 1:
                    oddCount += 1
                    if oddCount > 1:
                        return False
            return True

        def traverse(node, ans, numCounts):
            if node == None:
                return 0
            if node.val in numCounts:
                numCounts[node.val] += 1
            else:
                numCounts[node.val] = 1

            if node.left == node.right == None:
                if checkPath(numCounts):
                    ans += 1
            else:
                ans += traverse(node.left, ans, numCounts) + \
                    traverse(node.right, ans, numCounts)
            numCounts[node.val] -= 1
            return ans

        numCounts = {}
        return traverse(root, 0, numCounts)
