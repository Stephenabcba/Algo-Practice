// leetcode problem #1721. Swapping Nodes in a Linked List
/*
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
*/

/*
My Solution:
Idea:
1. find the kth node from the front
2. find the length of the list
3. find the (length-k)th node from the front
4. swap the value of nodes in (1) and (3)
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
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function (head, k) {
    // find the front node
    let frontNode = head
    for (let i = 0; i < k - 1; i++) {
        frontNode = frontNode.next
    }

    // find the length of the SLL
    let length = k
    let runner = frontNode.next
    while (runner != null) {
        runner = runner.next
        length++
    }

    // find the (length-k)th node from the front
    let backNode = head
    for (let j = 0; j < length - k; j++) {
        backNode = backNode.next
    }

    // swap the values of front and back node
    let temp = frontNode.val
    frontNode.val = backNode.val
    backNode.val = temp
    return head
};

/*
Test Cases:
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
*/

/*
Refactoring idea from discussion by longluo:
steps 1 & 4 are the same
steps 2 & 3 can be refactored:
    - the front node is already offset by K elements from the front
    - if an "end" pointer starts at front node and the back node pointer starts at the head:
        -> when the end pointer reaches the back of the SLL, the back pointer is k-offset from the back

*/

var swapNodes2 = function (head, k) {
    // find the front node
    let frontNode = head
    for (let i = 0; i < k - 1; i++) {
        frontNode = frontNode.next
    }

    // find the back node with an offset pointer
    let backNode = head
    let endNode = frontNode
    while (endNode.next != null) {
        backNode = backNode.next
        endNode = endNode.next
    }

    // swap the values of front and back node
    let temp = frontNode.val
    frontNode.val = backNode.val
    backNode.val = temp
    return head
};