# leetcode problem # 3016. Minimum Number of Pushes to Type Word II

"""
You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png

Example 1:
https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png
Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

Example 2:
https://assets.leetcode.com/uploads/2023/12/26/keypadv2e2.png
Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

Example 3:
https://assets.leetcode.com/uploads/2023/12/27/keypadv2.png
Input: word = "aabbccddeeffgghhiiiiii"
Output: 24
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.

Constraints:
1 <= word.length <= 10^5
word consists of lowercase English letters.
"""

"""
My solution: Count then Sort

Idea: The most frequent letters in a word should be assigned to the least number of button presses

Logic:
1. Count the frequency of each letter
    - in this implementation, the frequencies are stored in a list
2. Sort the frequencies
3. Assign the button presses
    - The first 8 (indexes 0-7) most frequent letters are assigned to 1 button press
    - The second 8 (indexes 8-15) most frequent letters are assigned to 2 button presses
    - The same logic applies to the third 8 and the last 2
4. Return the total presses used

Runtime: O(N + k * logk) Where N is the length of the word, and k is the size of the set of available letters
Space: O(k)
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        letterCounts = [0] * 26

        for letter in word:
            letterIdx = ord(letter) - ord('a')
            letterCounts[letterIdx] += 1

        letterCounts.sort(reverse=True)

        ans = 0

        for idx in range(26):
            if letterCounts[idx] > 0:
                ans += letterCounts[idx] * (idx // 8 + 1)
            else:
                break

        return ans
