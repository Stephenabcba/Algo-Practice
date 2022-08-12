// leetcode problem # 235. Lowest Common Ancestor of a Binary Search Tree

/*
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:
https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the BST.
*/

/*
My solution: Iteratively traverse the tree

Observations: 
1. The value of the LCA node of a BST is always between the two target nodes
- It's also allowed that LCA is one of the target nodes

2. If the current node is larger than both target nodes, the left child of the current node is closer to the LCA.
3. If the current node is smaller than both target nodes, the right child of the current node is closer to the LCA.

From the 3 observations above, there is a deterministic path between the root of the BST to the LCA. Thus, recursion is not required.

Runtime: O(N) where N is the number of nodes in the BST
- in the worst case, the BST could be shaped like a singly-linked list with the target node at the end, and the algorithm has to traverse through all the nodes to reach the LCA.
Space: O(1), solution memory usage does not depend on input size.

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
    while (root !== null) {
        if (p.val < root.val && q.val < root.val) {
            root = root.left
        } else if (p.val > root.val && q.val > root.val) {
            root = root.right
        } else {
            // if the node is between the two nodes or equal to one of the nodes, the node is the LCA.
            return root
        }
    }
    // this statement should not be reached.
    return null
};