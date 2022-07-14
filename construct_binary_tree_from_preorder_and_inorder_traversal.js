// leetcode problem # 105. Construct Binary Tree from Preorder and Inorder Traversal

/*
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

additional test cases: (first line is preorder, and second line is inorder)
[1,2,4,5,3]
[4,2,5,1,3]

[5,4,3,2,1,6]
[1,2,3,4,5,6]

[1,2,3,4,5]
[2,3,1,4,5]

[1,2,3,4,5,6,7,8,9,10,11,12]
[6,5,4,3,2,1,7,10,9,12,11,8]

[4,1,2,3]
[1,2,3,4]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
*/

/*
My solution: iterate through the preorder array, and confirm the node's location using inorder array

Reminder:
preorder traversal follows the Node, Left, Right pattern
inorder traversal follows the Left, Node, Right pattern

Every node in the tree (except the root) can either be:
- a left child of a node (inorder index of node < parent)
    - based on the preorder traversal pattern, the node must be the left child of the previous node in preorder traversal.
- a right child of a node (inorder index > parent)
    - the node could be the child of any node in the currently travelled path.

Idea:
Iterate through every node in preorder array
- keep track of the path traversed 
    - can be done with a stack (implemented with an array in solution)
- if the current node is a left child, add it as the left child of the previous node
- if the current node is a right child, determine which node in the path the node is the right child of
    - starting from the root, find the first node in the traversed path where the current node
        is to the right of the node in inorder traversal, and the node has no right child yet


Runtime: O(N * H) where N is the number of nodes in the tree, and H is the height of the tree
Space: O(N + H) where N is the number of nodes in the tree, and H is the height of the tree
- the dictionary / object created from the inorder traversal takes O(N) memory
- the stack takes O(H) memory
- as H <= N, the space complexity can be simplified to O(N)
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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
    // convert the inorder array to an object for O(1) lookup
    let inorderObj = {}
    for (let i = 0; i < inorder.length; i++) {
        inorderObj[inorder[i]] = i
    }

    // initialize the root of the tree and the stack keeping track of the path taken to reach the node
    let root = new TreeNode(preorder[0])
    let stack = []
    stack.push(root)

    for (let i = 1; i < preorder.length; i++) {
        let newNode = new TreeNode(preorder[i])
        // if the current node is to the left of the previous node in inorder traversal, the current node is the left child of the previous node.
        if (inorderObj[preorder[i]] < inorderObj[stack[stack.length - 1].val]) {
            stack[stack.length - 1].left = newNode
        } else {
            // the current node is a right child. determine which node the current node is the right child of
            // starting from the root, find the first node in the traversed path where the current node
            //   is to the right of the node in inorder traversal, and the node has no right child yet
            for (let j = 0; j < stack.length; j++) {
                if (inorderObj[preorder[i]] > inorderObj[stack[j].val] && stack[j].right === null) {
                    let startLength = stack.length
                    for (let k = 0; k < startLength - j - 1; k++) {
                        stack.pop()
                    }
                    break
                }
            }
            stack[stack.length - 1].right = newNode
        }
        // add the current node to the traversed path
        stack.push(newNode)
    }


    return root
};