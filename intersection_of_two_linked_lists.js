// leetcode problem # 160. Intersection of Two Linked Lists

/*
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
https://assets.leetcode.com/uploads/2021/03/05/160_statement.png
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.


Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
*/

/*
My solution: Align the end of the SLLs

Observation: if the input SLLs intersect, they share all nodes from the intersecting node to the end

Idea:
If the SLL could be traversed from tail to head, the algorithm is as simple as traversing the two lists backwards simultaneously until the earliest node that matches

However, as the SLL can only be traversed from head to tail, modifications must be made.

By aligning a pointer on each SLL such that the distance from each pointer to the end of its respective SLL is equal,
the solution is a linear process of finding the first node on each SLL that matches. This node is the intersection.

Runtime: O(M+N), where M and N are the lengths of the SLLs
Memory: O(1), The space used is independent of input size.

*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
    // don't process the lists if either list is empty.
    if (headA == null || headB == null) {
        return null
    }

    // initialize the pointers and lengths
    let curA = headA
    let curB = headB

    let lenA = 1
    let lenB = 1

    // find the last nodes of the lists and their lengths
    while (curA.next != null) {
        lenA++
        curA = curA.next
    }

    while (curB.next != null) {
        lenB++
        curB = curB.next
    }

    // if the last nodes do not match, the lists did not intersect
    if (curA != curB) {
        return null
    }

    // if the last nodes did match, the lists did intersect

    // align the lists by their tails
    // =>move the pointer of the longer list until its distance from the tail is the same as the length of the shorter list
    // if the lists are the same length, this step is skipped.
    curA = headA
    curB = headB

    if (lenA > lenB) {
        for (let i = 0; i < lenA - lenB; i++) {
            curA = curA.next
        }
    } else if (lenB > lenA) {
        for (let i = 0; i < lenB - lenA; i++) {
            curB = curB.next
        }
    }

    // at this point, the two lists must intersect at some point due to the observation.
    // traverse until the intersection happens.
    while (curA != curB) {
        curA = curA.next
        curB = curB.next
    }
    return curA
};

/*

Example 1:
https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
*/