// Leetcode problem # 141. Linked List Cycle
/*
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
*/
/*
Note: there is a special mathematical proof that if a linked list is a cycle, 
a runner moving 2 spaces every step will eventually catch up to a walker moving 1 space every step.
*/


/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
    let runner = head
    let walker = head
    while (runner) {
        if (runner.next && runner.next.next) {
            runner = runner.next.next
        } else {
            return false
        }
        walker = walker.next
        if (runner === walker) {
            return true
        }
    }
    return false
};