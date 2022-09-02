// leetcode problem # 230. Kth Smallest Element in a BST


/*
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

ex: if the kth smallest node has the value of 100, return 100

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
*/

/*
My Solution: Recursive in-order traversal
In-order traversal: check the left child, check the current node, and then check the right child.
    - with recursive relations, the left side of the tree is traversed before the root, and then the right side of the tree
The traversal will build up to the kth smallest node
    - for simplicity, the recursive function returns an array
        - the value at index one indicates whether the kth node has been reached
            - true if reached, false if not
        - the value at index 0 depends on the other return value
            - if kth node is reached, it is the actual value to return
            - if kth node is not reached, it is the relative kth node of the left child
    - in this solution, when searching for the right child, the algorithm searches for the k - position of the parent
        - this way, the recursive function does not need a third parameter
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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
    const findPosition = (curNode, k) => {
        if (curNode == null) {
            return [0, false]
        }
        let result = findPosition(curNode.left, k)
        // console.log(result)
        if (result[1]) {
            return result
        }
        let curPosition = 1 + result[0]
        if (curPosition == k) {
            return [curNode.val, true]
        }
        let rightResult = findPosition(curNode.right, k - curPosition)
        if (rightResult[1]) {
            return rightResult
        }
        return [curPosition + rightResult[0], false]
    }
    return findPosition(root, k)[0]
};

const root = { val: 6, left: null, right: null }
root.left = { val: 2, left: null, right: null }
root.left.right = { val: 4, left: null, right: null }
root.right = { val: 8, left: null, right: null }

for (let i = 1; i < 5; i++) {
    console.log("result:", kthSmallest(root, i))
}

/*
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
*/