# leetcode problem # 1669. Merge In Between Linked Lists

"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:
https://assets.leetcode.com/uploads/2020/11/05/fig1.png

Build the result list and return its head.

Example 1:
https://assets.leetcode.com/uploads/2024/03/01/ll.png
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:
https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

Constraints:
3 <= list1.length <= 10^4
1 <= a <= b < list1.length - 1
1 <= list2.length <= 10^4
"""

"""
My solution: Find the connection points and connect

To properly connect the list as instructed, 4 nodes are required
1. the a-1th node
2. the head of list 2
3. the tail of list 2
4. the b+1th node

To find the 4 nodes, traverse through lists 1 and 2
- traverse through list 1, stop at a-1th node, save a pointer
- continue traversing through list 1 to b+1th node, save a pointer
- the head of list 2 is already given
- traverse through the list 2 until the tail is reached, save a pointer

Connections: 
1. a-1th node connects to head of list 2
2. the tail of list 2 connects to a+1th node

The ath to bth nodes are now disconnected from the list, and can be discarded

Return list1 at the end

Runtime: O(N) where N is the total number of nodes
Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx1 = 0
        curNode1 = list1

        while idx1 < a - 1:
            idx1 += 1
            curNode1 = curNode1.next

        connectLeft = curNode1

        while idx1 < b:
            idx1 += 1
            curNode1 = curNode1.next

        connectRight = curNode1.next

        curNode2 = list2
        while curNode2.next:
            curNode2 = curNode2.next

        connectLeft.next = list2
        curNode2.next = connectRight

        return list1
