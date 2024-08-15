# leetcode problem # 860. Lemonade Change

"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Example 1:
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

Constraints:
1 <= bills.length <= 10^5
bills[i] is either 5, 10, or 20.
"""

"""
My solution: Process each customer

Logic:
1. Keep count of the current change available
2. Process each customer
    - if the correct change can be provided, accept the bill and update the change
    - otherwise, return False
    *If the customer provides a $20 bill, prioritize providing a $10 with a $5 over three $5
3. Return True if all customers have been served

Runtime: O(N) where N is the number of customers
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0] * 3

        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if change[0] == 0:
                    return False
                change[0] -= 1
                change[1] += 1
            else:
                required = 3
                if change[1] > 0:
                    required -= 2
                    change[1] -= 1
                if change[0] < required:
                    return False
                change[0] -= required
                change[2] += 1

        return True
