# leetcode problem # 2405. Optimal Partition of String

"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.


Example 1:
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

Constraints:
1 <= s.length <= 10^5
s consists of only English lowercase letters.
"""

"""
My Solution: Greedy

Intuition:
As the string is split into substrings, the order of the letters cannot be changed.
Thus, using a greedy approach where every partition includes as many letters as possible
leads to the optimal solution.

A set can be used to keep track of the letters in the partition.
If a letter is already in the set, a new partition needs to be created.

Logic:
1. Iterate through each letter
- if the letter has occurred before in the partition, create a new partition with only the
current letter.
- otherwise, add the current letter to the partition
2. Return the number of partitions created

Runtime: O(N) where N is the number of letters in s
Space: O(1), memory usage does not depend on input (it is always fixed by the character set,
        which is 26 in this case)
"""


class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1

        letters = set()

        for letter in s:
            if letter in letters:
                partitions += 1
                letters = set()
            letters.add(letter)

        return partitions
