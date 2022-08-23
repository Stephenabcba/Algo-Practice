// leetcode problem # 234. Palindrome Linked List

/*
Given the head of a singly linked list, return true if it is a palindrome.


Example 1:
https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg
Input: head = [1,2,2,1]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg
Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
*/

/*
My solution: convert to array then process
- By converting the SLL into an array, the process of checking if the list is a palindrome becomes simple
    -> just check if the first N/2 values are the same as the next N/2 values in reversed order one by one

Runtime: O(N) where N is the length of the SLL
Space: O(N) where N is the length of the SLL
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
 * @return {boolean}
 */
var isPalindrome = function (head) {
    let arr = []

    while (head !== null) {
        arr.push(head.val)
        head = head.next
    }

    for (let i = 0; i < arr.length / 2; i++) {
        if (arr[i] != arr[arr.length - i - 1]) {
            return false
        }
    }

    return true
};

/*
From leetcode discussion by luluboy168:
To achieve O(1) memory usage, reverse the second half of the SLL
Then check if the first half is the same as the second half
*/