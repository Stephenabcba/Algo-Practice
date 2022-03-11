// Leetcode problem #61. Rotate List
// Given the head of a linked list, rotate the list to the right by k places.
/*
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
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
var rotateRight = function (head, k) {
    // edge cases: 
    // SLL is empty, nothing to rotate
    // k is 0: no need to rotate
    if (head === null || k === 0) {
        return head
    }

    // find out length of SLL
    let listLength = 0
    let runner = head
    while (runner) {
        listLength++
        runner = runner.next
    }

    // effective rotation is the remainder of k / listLength
    // rotating the SLL by whole number multiples of listLength
    //   results in the same SLL
    const effectiveK = k % listLength

    // if effectiveK is 0, there is no rotation required
    if (effectiveK == 0) {
        return head
    }

    // look for the node before the new head, to sever the link
    let newHeadPrevRunner = head
    for (let i = 0; i < listLength - effectiveK - 1; i++) {
        newHeadPrevRunner = newHeadPrevRunner.next
    }

    // assign the new head and sever the link
    const newHead = newHeadPrevRunner.next
    newHeadPrevRunner.next = null

    // reconnect the SLL to the old head
    let connectRunner = newHead
    while (connectRunner.next) {
        connectRunner = connectRunner.next
    }
    connectRunner.next = head

    return newHead
};