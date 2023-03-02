# leetcode problem # 443. String Compression

"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

"""
My solution: remove excess characters and keep count

Logic:
1. Remove any repeating characters and keep count of the characters in the substring
    - ex: if there is a substring "aaaaaaaa" (8 a's), remove the extra 7 a's, and keep
    the count (8)
2. If the next letter is a different letter, add the count to the array before moving to
the next letter
    - ex: the current letter is "a" while the next letter is "b", add the count (8) so that
    the array loos like [...,"a", "8", "b", ...]
    - if the count == 1, do not add the count to the array
    - if the count has more than 2 digits, add each digit separately
        - ex: if count is 123, the array would be: [..., "1", "2", "3", ...]
3. Repeat steps 1 and 2 until the string is compressed

Runtime: O(N^2) where N is the number of items in the chars array
Space: O(1) Memory usage does not depend on input
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        count = 1
        while idx < len(chars):
            if idx < len(chars) - 1 and chars[idx + 1] == chars[idx]:
                chars.pop(idx + 1)
                count += 1
            else:
                if count == 1:
                    idx += 1
                else:
                    increment = 0
                    while count > 0:
                        curNum = count % 10
                        chars.insert(idx + 1, str(curNum))
                        count = count // 10
                        increment += 1
                    idx += increment + 1
                    count = 1

        return len(chars)
