# leetcode problem # 382. Linked List Random Node

"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.


Example 1:
https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.


Constraints:
The number of nodes in the linked list will be in the range [1, 10^4].
-10^4 <= Node.val <= 10^4
At most 10^4 calls will be made to getRandom.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?
"""

"""
My solution: Convert SLL to list then get random

In a list format, every value in the list can be accessed in constant time.

Using the random module, a random index can be selected from the list and returned every time

Runtime: O(N + M) where N is the number of elements in the SLL, and M is the number of calls to getRandom()
Space: O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




from random import randint
class Solution:

    def __init__(self, head: Optional[ListNode]):
        curNode = head
        nums = []
        while curNode is not None:
            nums.append(curNode.val)
            curNode = curNode.next
        self.nums = nums

    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
Solution in LeetCode Editorial: Reservoir Sampling

Reservoir sampling is able to keep a reservoir of k chosen elements, where k = 1
in this problem.

Leetcode uses Algorithm R by Alan Waterman, which is as follows:
1. Initialize the first k elements to be the reservoir R
2. Iterate the rest of the elements from k+1 to n
- for each index i, generate a random integer j where 1 <= j <= i
- if j <= k, replace R[j] with the element at i in the SLL
3. At the end, all values in R are the chosen values

It can be mathematically proven that the chance any element ends up in the reservoir
is equal to each other, and is equal to k / n.

Runtime:
init(): O(1), init time does not depend on input
getRandom(): O(N), where N is the length of the input SLL
overall: O(M * N), where N is legnth of SLL, and M is the number of times that getRandom() is called.

Space: O(1), memory usage does not depend on input
"""


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value
