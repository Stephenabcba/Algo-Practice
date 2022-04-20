// leetcode problem # 173. Binary Search Tree Iterator

/*
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
0 <= Node.val <= 10^6
At most 10^5 calls will be made to hasNext, and next.

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
*/


/*
My Solution:
follow the binary search tree logic
find the smallest number that is greater than the previous value

Runtime: O(M * log N) for M calls of next() and N nodes in the BST
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
 */
var BSTIterator = function (root) {
    this.root = root
    this.prevVal = -Infinity
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function () {
    let found = false
    let curNode = this.root
    let returnVal = Infinity
    while (curNode) {
        if (curNode.val > this.prevVal && curNode.val < returnVal) {
            returnVal = curNode.val
        }
        if (this.prevVal < curNode.val) {
            curNode = curNode.left
        } else if (this.prevVal >= curNode.val) {
            curNode = curNode.right
        }
    }
    this.prevVal = returnVal
    return returnVal
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function () {
    let found = false
    let curNode = this.root
    let returnVal = Infinity
    while (curNode) {
        if (curNode.val > this.prevVal && curNode.val < returnVal) {
            returnVal = curNode.val
        }
        if (this.prevVal < curNode.val) {
            curNode = curNode.left
        } else if (this.prevVal >= curNode.val) {
            curNode = curNode.right
        }
    }
    return returnVal != Infinity
};

/** 
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */

/*
Example 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
*/