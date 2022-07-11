// leetcode problem # 199. Binary Tree Right Side View

/*
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


Example 1:
https://assets.leetcode.com/uploads/2021/02/14/tree.jpg
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
*/

/*
My solution: Recursive traversal favoring the right side first
The traversal follows the Node, Right, Left pattern
    - the furthest right branch is visited first, and the furthest left branch is visited last.
Based on the traversal pattern above, the first node visited on each level is the right most node of the level.
    - these first nodes are the nodes "seen" from the right side
    - add the nodes to the answer

Runtime: O(N), where N is the number of nodes in the binary tree
Space: O(H), where H is the height of the tree
    - the memory usage of creating new recursive functions is not included.
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
 * @return {number[]}
 */
var rightSideView = function (root) {
    let ans = []
    let traverseTree = (curNode, level, ans) => {
        if (curNode === null) {
            return
        }
        if (level > ans.length) {
            ans.push(curNode.val)
        }
        traverseTree(curNode.right, level + 1, ans)
        traverseTree(curNode.left, level + 1, ans)
    }
    traverseTree(root, 1, ans)
    return ans
};