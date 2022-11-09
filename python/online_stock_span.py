# leetcode problem # 901. Online Stock Span

"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.


Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6

Constraints:

1 <= price <= 10^5
At most 10^4 calls will be made to next.
"""

"""
My solution: Use a stack to keep track of the prices

Observation: if yesterday's price is higher than today's price, the span is 1
- this is true regardless of how many values in the past were lower than today's price

Observation 2: The solution only cares about how many values are lower, not how much they are lower by
- The prices can be grouped into counts without losing important information

Data structure to hold the information: stack
- each item in the stack holds the price and the span of the price (the number of items that were consecutively lower than the price)
- Cases that can happen when .next() is called:
    1. If the stack is empty or today's price is lower than yesterday's price:
        - the span is 1
        - push [price, 1] to the stack
    2. If the stack is not empty and today's price is higher than yesterday's price:
        - pop from the stack until today's price is lower than top of the stack
            - or until the stack is empty
        - sum up the span of all items popped
        - the span is 1 + sum of spans popped
        - push [price, span] to the stack

Runtime: O(N) where N is the number of times .next() is called
- pushing to the stack happens N times exactly
    - every call of .next() always pushes once
- popping from the stack can happen up to N times in total
    - it is impossible to pop more times than the number of times pushed
Space: O(N) where N is the number of times .next() is called
"""


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if len(self.stack) == 0 or price < self.stack[-1][0]:
            self.stack.append([price, 1])
            return 1

        span = 1
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]

        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
