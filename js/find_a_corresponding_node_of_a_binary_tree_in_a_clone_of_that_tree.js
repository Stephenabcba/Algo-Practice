// leetcode problem # 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

/*
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.



Constraints:

The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.

Follow up: Could you solve the problem if repeated values on the tree are allowed?
*/

/*
My Solution: Searching the original tree and retracing the steps in the cloned tree
Part 1: Search through the original tree
- DFS is used here
- As the binary tree is not always a BST, worst case runtime is O(N), where N is all the nodes
- the path is saved to an array, where -1 is left and 1 is right
    - this array is used for part 2
    - when completed, the path saves all the steps required to navigate to the target from the root
        - there is exactly 1 path to the target node, as there is no way of traversing to a parent node from a child node.
- The algorithm compares the current node to the target node by address, so the follow-up is also satisfied

Part 2: Retracing the exact path in the cloned tree
- follow the path saved in part 1 step-by-step starting from the root
    - traverse left if the current value is -1
    - traverse right if the current value is 1
- when all the steps have been completed, the current node is the target node in the cloned tree.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} original
 * @param {TreeNode} cloned
 * @param {TreeNode} target
 * @return {TreeNode}
 */

var getTargetCopy = function (original, cloned, target) {
    // tree search logic
    const searchOriginal = (original, target, path) => {
        if (original === null) {
            return false
        }
        if (original === target) {
            return true
        }

        path.push(-1)
        const leftResult = searchOriginal(original.left, target, path)
        if (leftResult == false) {
            path.pop()
        }

        path.push(1)
        const rightResult = searchOriginal(original.right, target, path)
        if (rightResult == false) {
            path.pop()
        }
        return leftResult || rightResult
    }

    // search the tree
    const path = []
    searchOriginal(original, target, path)

    // retrace the steps
    let curNode = cloned
    for (let step of path) {
        if (step < 0) {
            curNode = curNode.left
        } else {
            curNode = curNode.right
        }
    }

    return curNode
};

/*
Example 1:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
https://assets.leetcode.com/uploads/2020/02/21/e1.png

Example 2:
Input: tree = [7], target =  7
Output: 7
https://assets.leetcode.com/uploads/2020/02/21/e2.png

Example 3:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
https://assets.leetcode.com/uploads/2020/02/21/e3.png
*/