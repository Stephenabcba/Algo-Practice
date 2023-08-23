# leetcode problem # 767. Reorganize String

"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

"""
My solution: Greedily place the most frequent letters

Idea:
To ensure that letters can all be placed without repeating adjacent characters, place the most frequent letters
first.

A heap can be used to keep track of the letters with the highest count
- when a letter is used, don't add it back to the heap immediately
    - this makes sure that adjacent characters aren't repeated

Logic:
1. Keep a count of letters in s
2. Insert non-zero counts into the heap
3. iterate until the heap is empty:
    i. remove a value from heap
        - if there was a holder value, reinsert the value into the heap
    ii. add the letter from (i) to the final answer
    iii. decrement count for the letter
    iv. save the letter and count to the holder variable
4. if the holder is not empty, the operation didn't succeed; return empty string
    - otherwise, return the created string

Runtime: O(N * logk) where N is length of string S and k is the size of character set (26 in this case)
Space: O(k)
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []

        letterCount = [0] * 26

        for letter in s:
            letterCount[ord(letter) - ord("a")] += 1

        for idx, count in enumerate(letterCount):
            if count > 0:
                heap.append([-count, chr(idx + ord("a"))])

        heapq.heapify(heap)

        ans = ""

        prev = None
        prevCount = 0

        while len(heap) > 0:
            curCount = 0
            cur = None
            if prev is not None:
                curCount, cur = heapq.heapreplace(heap, [-prevCount, prev])
            else:
                curCount, cur = heapq.heappop(heap)
            curCount = -curCount

            ans += cur
            curCount -= 1

            prev = cur
            prevCount = curCount
            if prevCount == 0:
                prev = None

        if prev:
            return ""

        return ans
    

"""
Solution by leetcode: Counting and Odd/Even

The solution recognizes an important fact: the input has a valid solution if
and only if the most frequent letter can be placed
- if the most frequent letter can be placed, the input will always have a solution
    - the rest of the work simply places values into the output
- if the most frequent letter can't be place, the input doesn't have a solution
    - no more work needs to be done

The most frequent letter can be placed if its count <= ceil(len(s) / 2)
- ex: if len(s) == 5 and most frequent letter has count of 3, the letter can be placed
    - if the count is 4, the letter can't be placed
- ex: if len(s) == 10 and most frequent letter has count of 5, the letter can be placed

Logic:
1. Collect count of all letters in s
2. Find the most frequent letter
3. Check if the most frequent letter can be placed
    - if it can't be placed, return empty string
4. Create a list with length of len(s), filled with empty strings
5. If it can be placed, place the most frequent letter on all even spaces until
all counts of the letter have been placed
6. Continue placing the rest of the letters
- when all even spaces are occupied, start placing the letters in odd spaces
- it doesn't matter which letter is placed first, but place the same letters until
    are placed
7. Combine the list and return the resulting string

Runtime: O(N)
Space: O(k)
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        max_count, letter = 0, ''
        for char, count in char_counts.items():
            if count > max_count:
                max_count = count
                letter = char
        if max_count > (len(s) + 1) // 2:
            return ""
        ans = [''] * len(s)
        index = 0

        # Place the most frequent letter
        while char_counts[letter] != 0:
            ans[index] = letter
            index += 2
            char_counts[letter] -= 1

        # Place rest of the letters in any order
        for char, count in char_counts.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return ''.join(ans)