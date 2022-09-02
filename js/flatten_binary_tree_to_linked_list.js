// leetcode problem # 114. Flatten Binary Tree to Linked List

/*
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
*/

/*
My solution: Recursion
Base Case: reached a branch of the binary tree; stop recursing 
Recursive Cases:
1. Node exists with no left node
- keep traversing to the right side
    - if right side doesn't exist, the recursion will trigger base case.
2. Node exists with left node
- "flatten" the left side
- move the left side to the right
- reconnect the end of the left side to the start of the right side (of current node)
- continue traversing to the right side

In order to keep track of the connection point between the flattened left side and the right side, the recursive function has a return value
- the returned value is always the deeped node reached from the current node
    - this node is the node that will connect to the right side of the tree (when needed)

Runtime: O(N) where N is the number of nodes in the binary tree
Space: O(1), memory usage does not depend on input size
- this omits the memory usage of recursive functions
    - if the recursive function memory usage is factored in, it's O(N) where N is the number of nodes in the binary tree
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
var flatten = function (root) {
    let recurse = (node) => {
        // base case: reached a branch (node is null)
        if (node === null) {
            return node
        }

        // use this variable to find the end of a flattened left branch
        let returnNode = node

        // if there's no left node, keep going to the right side
        if (node.left === null) {
            let returnedNode = recurse(node.right)
            if (returnedNode != null) {
                returnNode = returnedNode
            }
        } else { // if there's a left node, flatten the left node and attach the right node to the end of the flattened left side
            let temp = node.right
            node.right = node.left
            node.left = null
            let returnedNode = recurse(node.right)
            if (returnedNode === null) {
                node.right = temp
            } else {
                returnNode = returnedNode
                returnNode.right = temp
            }
            returnedNode = recurse(temp)
            if (returnedNode !== null) {
                returnNode = returnedNode
            }
        }
        return returnNode
    }

    recurse(root)
};