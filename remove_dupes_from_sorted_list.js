// leetcode # 82. Remove Duplicates from Sorted List II
/*
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. 
Return the linked list sorted as well.
Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
    //empty list: don't do anything
    if (!head) return head
    // head value is duplicated, double while loop handles multiple duplicated values at start
    let isDupe = false
    while (head && head.next && head.val == head.next.val) {
        while (head && head.next && head.val == head.next.val) {
            isDupe = true
            head = head.next
        }
        if (isDupe && head) {
            head = head.next
            isDupe = false
        }
    }
    if (isDupe && head) {
        head = head.next
        isDupe = false
    }
    // check if the value after runner is duplicated, repeat for all values in list
    let runner = head
    isDupe = false
    while (runner) {
        if (runner.next && runner.next.next && runner.next.val == runner.next.next.val) { // more duplicates to remove
            runner.next = runner.next.next
            isDupe = true
        } else {
            if (isDupe && runner.next) { // remove last duplicated value
                runner.next = runner.next.next
                isDupe = false
            } else {
                runner = runner.next
            }
        }
    }
    return head
};