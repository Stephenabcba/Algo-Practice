// Leetcode problem #2. Add Two Numbers
/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
*/


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    let carriedDigit = 0
    const dummy = { next: null }
    let curNode = dummy
    while (l1 || l2 || carriedDigit) {
        const sumVals = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carriedDigit;
        l1 = l1?.next
        l2 = l2?.next
        curNode.next = new ListNode(sumVals % 10)
        carriedDigit = sumVals >= 10 ? 1 : 0
        curNode = curNode.next

    }
    return dummy.next
};