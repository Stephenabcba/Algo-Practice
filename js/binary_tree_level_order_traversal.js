// leetcode problem # 102. Binary Tree Level Order Traversal

/*
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Example 1:
https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
*/

/*
My solution: convert the binary tree into array of arrays and process like a queue

A binary tree can be converted into an 1D array by adding the children of each node to the array
1. Initialize the array and add the root node (if it exists) to the array
2. Iterate through the array like a queue, and add any children nodes to the back of the array
3. If iteration has reached the end of the array, all values have been added to the array.
* This method will add nodes to the array such that a parent level will always come before the child level.

The problem asks for the solution in the format of array of arrays, separated by level.
- The order of the nodes are the same, but now arrays have to be added
    - Simply add children nodes to a new array

To properly access each node's children, the address of each node is saved in the array of arrays first.
When all nodes have been processed, the address of each node is replaced by the actual values of each node.

Time: O(N) where N is the number of nodes in the binary tree
- each node is processed once
Space: O(N) where N is the number of nodes in the binary tree
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
 * @return {number[][]}
 */
var levelOrder = function (root) {
    let levels = []

    // if the root does not exist, do nothing.
    if (root !== null) {
        // the root is the only node on the first level
        levels.push([root])

        let level = 0
        while (level < levels.length) {
            levels.push([])
            // if any nodes on this level have children, add the children to the next level
            for (let node of levels[level]) {
                if (node.left !== null) {
                    levels[level + 1].push(node.left)
                }
                if (node.right !== null) {
                    levels[level + 1].push(node.right)
                }
            }
            // if no new nodes are added to the next level, remove the empty array
            if (levels[level + 1].length === 0) {
                levels.pop()
            }
            level += 1
        }

        // convert the values in the array of arrays from the nodes to their corresponding values.
        for (let row of levels) {
            for (let i = 0; i < row.length; i++) {
                row[i] = row[i].val
            }
        }
    }

    return levels
};