# leetcode problem # 846. Hand of Straights

"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:
1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

"""
My solution: Sort then solve

Sorting the hand allows grouping to be done in linear time

Logic:
1. Sort the hand
2. Iterate through each card
    i. group cards with the same values
        - when cards of the same value is seen, increment the count
    ii. when a new card with a different value is seen, process the previous cards
        - if the previous card value ends x groups, remove x cards from the count of the previous card
            - if there's not enough cards to end x groups, grouping cannot be done; return False
        - if there are still instances of the previous card, the current card's value cannot be more than the previous card's value + 1
        - after subtracting the number of cards used in the remaining unfinished groups, the remaining cards are used to create new groups
        - update the current card and its count (initially the count is 1)
3. Return True if the cards can be grouped (no conflicts in the grouping process)

Runtime: O(N*logN) where N is the size of the hand
Space: O(N)
"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        hand.sort()

        endings = deque()
        endingsCount = 0
        cur = hand[0]
        curCount = 1

        for idx in range(1, len(hand)):
            if hand[idx] == cur:
                curCount += 1
            else:
                if len(endings) > 0 and cur == endings[0][0]:
                    curCount -= endings[0][1]
                    endingsCount -= endings[0][1]
                    endings.popleft()

                if curCount < 0 or curCount > 0 and hand[idx] > cur + 1:
                    return False
                curCount -= endingsCount
                if curCount > 0:
                    endings.append([cur + groupSize - 1, curCount])
                    endingsCount += curCount
                cur = hand[idx]
                curCount = 1

        if len(endings) > 0 and cur == endings[0][0]:
            curCount -= endings[0][1]
            endings.popleft()
        if curCount != 0 or len(endings) > 0:
            return False

        return True
