// leetcode problem # 236. Lowest Common Ancestor of a Binary Tree

/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Example 1:
https://assets.leetcode.com/uploads/2018/12/14/binarytree.png
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
https://assets.leetcode.com/uploads/2018/12/14/binarytree.png
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.
*/

/*
My solution: Traverse the tree and find the first common ancestor

Traverse the tree in preorder (node, left, right) fashion. The first node to be the ancestor (including itself) of both nodes is the LCA.

Runtime: O(N) where N is the number of nodes in the tree
Memory: O(1), solution does not depend on input size
- This does not include the memory usage of recursive functions
    - there will be O(N) functions where N is the numebr of nodes in the tree
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
    let recurse = (node) => {
        let score = 0
        if (node === null) {
            return score
        }
        if (node == p || node == q) {
            score += 1
        }

        let left = recurse(node.left)
        let right = recurse(node.right)

        // if the LCA node is already found, return the node
        if (isNaN(left)) {
            return left
        }
        if (isNaN(right)) {
            return right
        }

        score += left + right
        // if the current node is the first node to be the ancestor of the given nodes, it is the LCA
        if (score == 2) {
            return node
        }

        // otherwise, return the number of nodes found
        return score
    }

    return recurse(root)
};