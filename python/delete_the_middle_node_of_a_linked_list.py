# leetcode problem # 2095. Delete the Middle Node of a Linked List

"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:
https://assets.leetcode.com/uploads/2021/11/16/eg1drawio.png
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
https://assets.leetcode.com/uploads/2021/11/16/eg2drawio.png
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
https://assets.leetcode.com/uploads/2021/11/16/eg3drawio.png
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:

The number of nodes in the list is in the range [1, 10^5].
1 <= Node.val <= 10^5
"""

"""
My solution: Slightly modified 2 pointer approach

Using 1 runner pointer (travels 2 nodes every iteration) and 1 walker node (travels 1 node every iteration), 
    the walker will land on the middle node when the runner node reaches the end of the SLL.

Modification: stop the walker from moving on the last iteration
- By moving the runner first, it is possible to check whether the runner has reached the end before moving the walker
- By witholding the last step of the walker, the walker will stop right before the middle node
    - Remove the middle node by simply setting walker.next to walker.next.next
        * watch out for edge case (explained below)

Edge case: Only 1 node in SLL:
- This is the only case where the head can be a middle node and must be deleted
- This case can be identified by checking if the walker is at the last node
    - in any other case, the walker will never reach the end of the SLL
        - ex: SLL = [1,2]:
            - the runner would move 2 nodes down into None, and walker would not move
- As the only node in the SLL is the head in this case, removing the head results in returning None.

Runtime: O(N) where N is the number of nodes in the SLL
- The iteration runs N/2 times as the runner skips a node every iteration

Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        walker = head

        while runner.next is not None:
            runner = runner.next.next

            if runner is None or runner.next is None:
                break

            walker = walker.next

        # edge case: only 1 node in the SLL
        if walker.next is None:
            return None

        walker.next = walker.next.next

        return head


"""
Solution from leetcode solution:

Same concept, but slightly different implementation
1. Check for the edge case first
2. Initialize runner to head.next.next
    - removes the need for the if statement
3. Change the while loop condition
    - while runner and runner.next instead of just runner.next
"""
