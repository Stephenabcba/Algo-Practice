// Leetcode problem # 21
// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
 var mergeTwoLists = function(list1, list2) {
    if (list1 === null && list2 === null) {
        return null
    }
    let returnList
    if (list1) {
        if (list2 && list2.val <= list1.val) {
            returnList = new ListNode(list2.val)
            list2 = list2.next
        } else {
            returnList = new ListNode(list1.val)
            list1 = list1.next
        }
    } else {
        returnList = new ListNode(list2.val)
        list2 = list2.next
    }
    let curNode = returnList
    while (list1 || list2) {
        if (list1) {
            if (list2 && list2.val <= list1.val) {
                curNode.next = new ListNode(list2.val)
                list2 = list2.next
            } else {
                curNode.next = new ListNode(list1.val)
                list1 = list1.next
            }
        } else {
            curNode.next = new ListNode(list2.val)
            list2 = list2.next
        }
        curNode = curNode.next
    }
    return returnList
};