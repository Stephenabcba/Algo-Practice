// leetcode problem # 98. Validate Binary Search Tree

/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg
Input: root = [2,1,3]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
*/

/*
My solution: Recursively validate the tree

Base Case: 
1. An empty node is always valid
    - by extension, a node with two empty children is valid
2. If a node is invalid, the entire tree is invalid, and no more recursion is needed.

Recursive Case: if a valid node has none-empty children, the children must be validated too

When searching the left subtree of a node, the values within the left subtree must not exceed the value of the node
When searching the right subtree of a node, the values within the right subtree must not be below the value of the node
Example:
- When a node A has a right child B with a left child C, the values must follow the rules of A < C < B for the tree to be valid.

From the rules above, the idea of upper and lower bound can be utilized.
- initialize the search process with unbound boundaries
- when searching the left subtree of a node, the upper bound is limited to the value of the node
- when searching the right subtree of a node, the lower bound is limited to the value of the node
- if a node's value is outside the allowed boundaries, the tree is invalid.

Runtime: O(N) where N is the number of nodes in the Binary Search Tree
Space: O(1) solution memory usage is independent of input size.
- this does not account for the memory usage of recursion
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
    let recurse = (node, lowerBound, upperBound) => {
        if (node === null) {
            return true
        }
        if (node.left !== null && (node.left.val >= node.val || node.left.val <= lowerBound) ||
            node.right !== null && (node.right.val <= node.val || node.right.val >= upperBound)) {
            return false
        }
        return recurse(node.left, lowerBound, node.val) && recurse(node.right, node.val, upperBound)
    }
    return recurse(root, -Infinity, Infinity)
};