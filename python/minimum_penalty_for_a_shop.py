# leetcode problem # 2483. Minimum Penalty for a Shop

"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.


Example 1:
Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

Example 2:
Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.

Example 3:
Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

Constraints:
1 <= customers.length <= 10^5
customers consists only of characters 'Y' and 'N'.
"""

"""
My solution: Prefix sum and suffix sum

Idea:
To calculate the penalty for closing at any given time interval i, two values are needed
1. the number of 'N' from the start to i (not including i) neeeds to be counted
2. the number of 'Y' from the end to i (including i) needs to be counted

The number of 'N' can be counted when iterating forwards, incrementing with every 'N'
- the 'N' is counted after deciding whether to close the store at i
The number of 'Y' can be counted by preprocessing the customers string backwards, storing the
count in a list with the same length of customers string

While iterating, keep track of the lowest penalty met and the index at which it happened
- at the end, check if closing at the very end incurs a lower penalty
- return the index

Runtime: O(N) where N is length of customers string
Space: O(N)
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minIndex = -1
        minPenalty = 1000000

        suffixY = [0] * len(customers)
        nCount = 0
        yCount = 0

        for idx in range(len(customers) - 1, -1, -1):
            if customers[idx] == "Y":
                yCount += 1
            suffixY[idx] = yCount

        for idx in range(len(customers)):
            penalty = nCount + suffixY[idx]
            if penalty < minPenalty:
                minIndex = idx
                minPenalty = penalty
            if customers[idx] == "N":
                nCount += 1
        
        if nCount < minPenalty:
            minIndex = len(customers)
            minPenalty = nCount
        
        return minIndex

"""
Slight improvement: Constant space solution

Upon further inspection, there is no need to hold an extra list for the number of "Y" after
time interval i; the data can be stored as a single integer and decremented when needed.

Runtime: O(N)
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minIndex = -1
        minPenalty = 1000000

        nCount = 0
        yCount = 0

        for idx in range(len(customers) - 1, -1, -1):
            if customers[idx] == "Y":
                yCount += 1

        for idx in range(len(customers)):
            penalty = nCount + yCount
            if penalty < minPenalty:
                minIndex = idx
                minPenalty = penalty
            if customers[idx] == "N":
                nCount += 1
            else:
                yCount -= 1
        
        if nCount < minPenalty:
            minIndex = len(customers)
            minPenalty = nCount
        
        return minIndex