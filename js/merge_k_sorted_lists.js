// Leetcode Problem #23. Merge k Sorted Lists
// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

// Example 1:

// Input: lists = [[1,4,5],[1,3,4],[2,6]]
// Output: [1,1,2,3,4,4,5,6]
// Explanation: The linked-lists are:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// merging them into one sorted list:
// 1->1->2->3->4->4->5->6

// Constraints:

// k == lists.length
// 0 <= k <= 10^4
// 0 <= lists[i].length <= 500
// -10^4 <= lists[i][j] <= 10^4
// lists[i] is sorted in ascending order.
// The sum of lists[i].length won't exceed 10^4.




class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if (lists.length === 0) {
        return null
    }
    let listsEmpty = true
    for (let list of lists) {
        if (list != null) {
            listsEmpty = false
            break
        }
    }
    if (listsEmpty) return null
    
    let listEmptyCheck = []
    let nonEmptyListCount = 0
    for (let list of lists) {
        if (list == null) {
            listEmptyCheck.push(0)
        } else {
            listEmptyCheck.push(1)
            nonEmptyListCount++
        }
    }
    let returnList = undefined
    let curNode = undefined
    while (nonEmptyListCount > 0) {
        let curMin = 1000000
        let curMinIndex = -1
        for (let index = 0; index < lists.length; index++) {
            if (listEmptyCheck[index] && lists[index].val < curMin) {
                curMin = lists[index].val
                curMinIndex = index
            }
        }
        if (returnList === undefined) {
            returnList = new ListNode(curMin)
            curNode = returnList
        } else {
            let newNode = new ListNode(curMin)
            curNode.next = newNode
            curNode = newNode
        }
        if (lists[curMinIndex].next != null) {
            lists[curMinIndex] =  lists[curMinIndex].next
        } else {
            listEmptyCheck[curMinIndex] = 0
            nonEmptyListCount --
        }
    }
    return returnList
};

function createList(numList) {
    let listHead = undefined
    let curNode = undefined
    for(let num of numList) {
        if (listHead === undefined) {
            listHead = new ListNode(num)
            curNode = listHead
        } else {
            let newNode = new ListNode(num)
            curNode.next = newNode
            curNode = newNode
        }
    }
    return listHead
}

function printList(nodeList) {
    let returnList = []
    while (nodeList != null) {
        returnList.push(nodeList.val)
        nodeList = nodeList.next
    }
    return returnList
}

let testList = createList([1,2,3,4,5])
// console.log(testList.val);
// console.log(printList(testList));
lists1 = [createList([1,4,5]),createList([1,3,4]),createList([2,6])]
console.log(printList(mergeKLists(lists1)));