# leetcode problem # 38. Count and Say

"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg
Given a positive integer n, return the nth term of the count-and-say sequence.


Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:
1 <= n <= 30
"""

"""
Solution: Following Hints and the recursive logic
Hint 1:
Create a helper function that maps an integer to pairs of its digits and their frequencies. 
For example, if you call this function with "223314444411", then it maps it to an array of pairs [[2,2], [3,2], [1,1], [4,5], [1, 2]].

Hint 2:
Create another helper function that takes the array of pairs and creates a new integer. 
For example, if you call this function with [[2,2], [3,2], [1,1], [4,5], [1, 2]], it should create "22"+"23"+"11"+"54"+"21" = "2223115421".

Hint 3:
Now, with the two helper functions, you can start with "1" and call the two functions alternatively n-1 times. 
The answer is the last integer you will obtain.

The helper function (function 1) from Hint 1 creates the components that make up the string for x + 1 given the string for x.
The helper function (function 2) from Hint 2 creates the actual string corresponding to the output of Hint 1.
Thus, starting from "1" (where x = 1), every call of function 1 in combination with function 2 creates the string for the x + 1 term.
-> Running the 2 functions n - 1 times will create the n-th term.

Under current logic, function 1 and function 2 can be refactored into a single function; the logic can build the new string while processing the previous string.


At first glance, it seems that following the recursive logic would result in a very slow runtime, 
especially since the resulting string for n = 30 has over 1000 characters.
However, LeetCode reported a runtime of 68ms for processing n = 30.

Runtime: ???; The length of the return string seems to grow faster than N^2
Space: ???; The length of the return string seems to grow faster than N^2
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        def createNextPair(inputStr):
            nextPair = []
            curDigit = ""
            frequency = 0
            for digit in inputStr:
                if digit is not curDigit:
                    if curDigit is not "":
                        nextPair.append([curDigit, frequency])
                    curDigit = digit
                    frequency = 1
                else:
                    frequency += 1
            nextPair.append([curDigit, frequency])
            return nextPair

        def convertToString(pairList):
            convertedString = ""
            for pair in pairList:
                convertedString += str(pair[1]) + pair[0]
            return convertedString

        if n == 1:
            return "1"

        curString = "1"

        for _ in range(n - 1):
            curString = convertToString(createNextPair(curString))

        return curString
