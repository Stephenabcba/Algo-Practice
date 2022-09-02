// leetcode problem # 108. Convert Sorted Array to Binary Search Tree

/*
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


Example 1:
https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg

Example 2:
https://assets.leetcode.com/uploads/2021/02/18/btree.jpg
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.
*/

/*
My solution: Recursively pick the middle node
By picking the middle node in the range every recursion, the remaining values are split in half in the left children and the right children, creating a height-balanced tree.
Using array indexing, no new arrays are created while recursing.

Runtime: O(N) where N is the number of values in the nums array
Space: O(N) where N is the number of values in the nums array
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
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function (nums) {
    let recurse = (nums, start, end) => {
        if (nums.length === 0 || start > end) {
            return null
        }
        let center = Math.floor((start + end) / 2)
        let newNode = new TreeNode(nums[center])
        newNode.left = recurse(nums, start, center - 1)
        newNode.right = recurse(nums, center + 1, end)
        return newNode
    }

    return recurse(nums, 0, nums.length - 1)
};