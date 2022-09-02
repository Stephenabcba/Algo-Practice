// leetcode problem # 99. Recover Binary Search Tree

/*
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1
*/

/*
Solution in leetcode discussion by shwetankverma23:
Inorder Traversal
- In a valid BST, inorder traversal produces a sorted array
    - a sorted array is in increasing order
- In this problem, 2 values are swapped, leading to 2 places in the array where the increasing order is violated
    - i.e. the value at an index is smaller than the value at the index before it
    - the first violation can be found where the value is larger than the index after it
    - the second violation can be found where the value is smaller than the index before it
- once the two nodes have been found, simply swap the value at the two nodes

- in his solution, the actual array is not required to solve the problem
    - only need to keep track of the previous value, and the 2 swapped nodes

Time: O(N) for N nodes in a BST
Space: O(1), only constant space is needed
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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function (root) {
    var prev = null
    var first = null
    var second = null

    const traverseTree = (root) => {
        if (root == null) {
            return null
        }
        traverseTree(root.left)
        if (prev != null && root.val < prev.val) {
            if (first == null) {
                first = prev
            }
            second = root
        }
        prev = root
        traverseTree(root.right)
    }
    traverseTree(root)
    let temp = first.val
    first.val = second.val
    second.val = temp
};

/*
Example 1: 
Input: root = [1,3,null,null,2] 
Output: [3,1,null,null,2] 
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid. 

Example 2: Input: root = [3,1,4,null,null,2] 
Output: [2,1,4,null,null,3] 
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

*/