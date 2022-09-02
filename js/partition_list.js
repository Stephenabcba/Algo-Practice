// leetcode problem # 86. Partition List


/*
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.


Example 1:
https://assets.leetcode.com/uploads/2021/01/04/partition.jpg
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
*/

/*
My solution: remove the out of place nodes, then replace them at their correct positions

Out of place nodes types:
1. all nodes greater than x but placed before node x
2. all nodes smaller than x but placed after node x

create a new SLL each for type 1 and type 2, then reconnect to the order:
nodes smaller than x before x -> nodes smaller than x after x -> nodes larger than or equal to x before x -> nodes larger than or equal to x after x

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1), memory usage does not depend on input size.

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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {
    let dummyHead = { next: head }
    let prev = dummyHead
    let cur = head

    // move all values before the first x node that is larger than x to a separate SLL
    let largerMoveStart = null
    let largerMoveEnd = null
    while (cur !== null && cur.val != x) {
        if (cur.val > x) {
            if (largerMoveStart === null) {
                largerMoveStart = cur
                largerMoveEnd = cur
            } else {
                largerMoveEnd.next = cur
                largerMoveEnd = largerMoveEnd.next
            }
            prev.next = cur.next
            cur.next = null
            cur = prev.next
        } else {
            prev = cur
            cur = cur.next
        }
    }

    // if X is not a node in the SLL, connect the original SLL (modified) to the larger nodes SLL.
    // the second portion of the solution is not needed.
    if (cur == null) {
        prev.next = largerMoveStart
        return dummyHead.next
    }

    // at this point, cur.val is x
    let smallerThanXEnd = prev

    prev = cur
    cur = cur.next

    // move all nodes after the first x node smaller than x to a separate SLL
    let smallerMoveStart = null
    let smallerMoveEnd = null
    while (cur !== null) {
        if (cur.val < x) {
            if (smallerMoveStart === null) {
                smallerMoveStart = cur
                smallerMoveEnd = cur
            } else {
                smallerMoveEnd.next = cur
                smallerMoveEnd = smallerMoveEnd.next
            }
            prev.next = cur.next
            cur.next = null
            cur = prev.next
        } else {
            prev = cur
            cur = cur.next
        }
    }

    // reconnect the SLLs in the correct order
    // order: smaller than x (before x) -> smaller than x (after x)
    //      -> larger than x (before x) -> larger than x (after x)
    let connectPoint = smallerThanXEnd

    if (smallerMoveStart !== null) {
        smallerMoveEnd.next = connectPoint.next
        connectPoint.next = smallerMoveStart
        connectPoint = smallerMoveEnd
    }

    if (largerMoveStart !== null) {
        largerMoveEnd.next = connectPoint.next
        connectPoint.next = largerMoveStart
    }

    return dummyHead.next


};

/*
Leetcode solution: keep two SLLs, then connect them
Keep track of all nodes with values smaller than x (SLL1)
Keep track of all nodes with values greater than or equal to x (SLL2)
attach the end of SLL 1 to start of SLL2

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1), memory usage does not depend on input size.
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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {
    let beforeHead = { next: null }
    let afterHead = { next: null }
    let before = beforeHead
    let after = afterHead

    while (head) {
        if (head.val < x) {
            before.next = head
            before = before.next
        } else {
            after.next = head
            after = after.next
        }
        head = head.next
    }

    // sever links after the new last node
    after.next = null

    before.next = afterHead.next

    return beforeHead.next
};