// leetcode problem # 669. Trim a Binary Search Tree

/*
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Constraints:
The number of nodes in the tree in the range [1, 10^4].
0 <= Node.val <= 10^4
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 10^4
*/

/*
My Solution: Recursive trimming
Base Cases:
the current node is null: return null

Recursive cases:
trim the left and right side of the tree

Trimming logic:
- recursively trim the children first
- if the current node is too large, return the trimmed left child
- if the current node is too small, return the trimmed right child
- if the current node is within bounds, return the node (both left and right children are already trimmed)

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
 * @param {number} low
 * @param {number} high
 * @return {TreeNode}
 */
var trimBST = function (root, low, high) {
    // base case: node is null
    if (root == null) {
        return null
    }

    // recursively trim the children
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    if (root.val < low) { // root value too small
        return root.right
    }
    if (root.val > high) { // root value too large
        return root.left
    }

    // root value within bounds
    return root
};


/*
Improvement from leetcode solution:
if the val of the parent node is out of bounds, only the left (or right) child needs to be processed
    - the other half of the tree do not need to be processed as it will definitely be out of bounds
*/
var trimBST2 = function (root, low, high) {
    if (root == null) {
        return null
    }

    if (root.val < low) {
        return trimBST(root.right, low, high)
    }
    if (root.val > high) {
        return trimBST(root.left, low, high)
    }

    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    return root
};