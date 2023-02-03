# leetcode problem # 6. Zigzag Conversion

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

"""
My solution: Follow the pattern

Depending on the number of rows, the zigzag pattern repeats after x letters,
where x = numRows * 2 - 2 as long as numRows > 1.
    - the first numRows letters are in their respective rows
    - the remaining letters are placed in reversed order, skipping the first and last
    row


To easily differentiate each row, the rows are stored separately and concatenating


Runtime: O(N) where N is the length of string s
Space: O(N)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]

        repeatLength = numRows * 2 - 2
        if numRows == 1:
            repeatLength = 1

        for idx in range(len(s)):
            curPos = idx % repeatLength
            if curPos < numRows:
                rows[curPos] += s[idx]
            else:
                rows[numRows * 2 - curPos - 2] += s[idx]

        ans = ""
        for row in rows:
            ans += row
        return ans