# leetcode problem # 1444. Number of Ways of Cutting a Pizza

"""
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:
https://assets.leetcode.com/uploads/2020/04/23/ways_to_cut_apple_1.png
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:
Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:
Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:
1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""

"""
My solution: Recursive DP

Intuition: Brute force solution is to try every single cut location possible
- if the combination of k-1 cuts can split the matrix into k portions of apples, it is a valid way of cutting
- However, to try every combination of cuts can take a very long time

Observation: given the same amount of leftover cuts and leftover portion of the matrix, the number of ways to cut the
matrix is fixed
    - In other words, how the previous cuts were made do not affect how the remaining matrix is cut, as long as the current
    state is the same
=> DP and memoization can be used to eliminate redundant processing

The DP matrix has 3 dimensions: Cuts, row, and col.
- Cuts is the number of remaining cuts needed to be used
    - the ways to cut a matrix depends on the number of cuts leftover
- row and col forms the coordinate of the top left piece of the remaining matrix to be cut
    - as the matrix can only be cut from the top and from the left, only 1 corner is needed to find the remaining matrix

* note that every combination must contain valid cuts
- if a combination includes an invalid cut, the combination is not valid
Here are the invalid cuts:
- the cut is made on the edge of the matrix, where the remaining matrix is out of bounds
- the cut does not leave at least 1 apple on both sides of the cut
    - if the cut does not leave an apple on the left side, it's possible that a cut from the top could be a valid cut
        - do not set the DP matrix in this case
    - if the cut does not leave an apple on the right or the bottom side, the cut is always invalid
        - set the DP matrix to 0 in this case

Runtime: O(M * N * C) where M is the number of rows and N is the number columns in the pizza, and C is the number of cuts
Space: O(M*N)
"""


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        numRows = len(pizza)
        numCols = len(pizza[0])
        modval = 1000000007
        apples = [[0 for _ in pizza[0]] for __ in pizza]
        dp = [[[-1 for _ in pizza[0]] for __ in pizza] for ___ in range(k)]

        if pizza[-1][-1] == "A":
            apples[-1][-1] = 1

        for col in range(numCols - 2, -1, -1):
            prev = apples[-1][col + 1]
            if pizza[-1][col] == "A":
                prev += 1
            apples[-1][col] = prev

        for row in range(numRows - 2, -1, -1):
            rowAppleCount = 0
            for col in range(numCols - 1, -1, -1):
                if pizza[row][col] == "A":
                    rowAppleCount += 1
                apples[row][col] = apples[row + 1][col] + rowAppleCount

        def cut(row, col, cuts, applesBeforeCut):
            if row >= numRows or col >= numCols or applesBeforeCut == apples[row][col]:
                return 0
            if dp[cuts][row][col] >= 0:
                return dp[cuts][row][col]
            if apples[row][col] == 0:
                dp[cuts][row][col] = 0
                return 0
            if cuts <= 0:
                dp[cuts][row][col] = 1
                return 1
            validWays = 0
            for i in range(row + 1, numRows):
                validWays += cut(i, col, cuts - 1, apples[row][col]) % modval
            for j in range(col + 1, numCols):
                validWays += cut(row, j, cuts - 1, apples[row][col]) % modval
            validWays = validWays % modval
            dp[cuts][row][col] = validWays
            return validWays

        return cut(0, 0, k - 1, -1)
