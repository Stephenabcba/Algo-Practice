// leetcode problem # 92. Reverse Linked List II

/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


Example 1:
https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
*/

/*
My solution: iteratively reverse the linked list with 3 pointers
By using 3 pointers (previous, current, and next node), the algorithm is able to process the nodes one by one and reverse the required portion
As not all nodes are reversed every time, the front and back portion needs to be reconnected to the reversed portion.

Note: the left and right indeces in input is 1-indexed.

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1), solution memory usage does not scale with SLL length
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
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
    // create a dummy head before the real head node
    // this dummy head takes care of the edge case of the head also being reversed
    // the head node in the end will always be the next node of the dummy head
    let dummyHead = { next: head }

    // keep track of the node before the reversal happens
    // this will be used to reconnect the reversed chain to the front portion
    let nodeBeforeLeft = dummyHead
    for (let i = 1; i < left; i++) {
        nodeBeforeLeft = nodeBeforeLeft.next
    }


    // keep track of the end of the reversed chain of nodes
    // this is also the first node to be reversed
    // this will be used to reconnect the reversed chain to the back portion
    let reversedEnd = nodeBeforeLeft.next

    let prevNode = nodeBeforeLeft.next
    let curNode = prevNode.next
    let nextNode = curNode ? curNode.next : null

    // keep track of next node in the forward direction
    // connect the current node to the previous node
    for (let i = 0; i < right - left; i++) {
        curNode.next = prevNode
        prevNode = curNode
        curNode = nextNode
        nextNode = curNode ? curNode.next : null
    }

    // reconnect the start and the end of the SLL to the reversed chain
    nodeBeforeLeft.next = prevNode
    reversedEnd.next = curNode

    return dummyHead.next
};