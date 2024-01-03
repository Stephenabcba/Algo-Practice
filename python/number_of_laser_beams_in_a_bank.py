# leetcode problem # 2125. Number of Laser Beams in a Bank

"""
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

Example 1:
https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg
Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.

Example 2:
https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg
Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows.

Constraints:
m == bank.length
n == bank[i].length
1 <= m, n <= 500
bank[i][j] is either '0' or '1'.
"""

"""
My solution: Count and math

the number of lasers between two neighboring rows is a * b
    - there are only empty rows between neighboring rows
    - a and b are the number of devices on the two rows

Logic:
1. Count the number of devices in a row
2. If the row is not empty, multiple the count with the number of devices in the last non-empty row
3. Repeat for all rows
4. Return the total

Runtime: O(M*N) where M and N are the number of rows and columns in the bank
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0

        prevCount = 0

        for row in bank:
            rowCount = 0
            for col in row:
                if col == "1":
                    rowCount += 1

            if rowCount > 0:
                ans += prevCount * rowCount
                prevCount = rowCount

        return ans
