# leetcode problem # 904. Fruit Into Baskets

"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

Constraints:
1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
"""

"""
My Solution: Keep track of the current 2 fruits in the baskets

Intuition: As only 2 types of fruits can be collected, the count of fruits
that can be collected from the current 2 fruits cannot increase anymore when 
a 3rd type of fruit is encountered.
- Keep track of whether the current count is the highest record
- Empty out the basket with the fruit that was less recent, and start filling it
with the 3rd fruit
    - ex. if fruits = [1,2,3], when fruit 3 is encountered, the basket with fruit 1
    is emptied.
- Also remove any fruits that was not consecutively collected
    - ex. if fruits = [2,2,1,2,3], when fruit 3 is encountered, two fruit 2 are also
    removed

Logic:
Iteratively process each fruit in order
- Case 1: Current basket is empty or the fruit is same as the fruits in the current basket
    - Increment the consecutively picked fruit count
        - these fruits are kept when a new fruit type is found
    - Increment the collected fruit count
- Case 2: Case 1 is false AND: Previous basket is empty or fruit is same as fruits in previous
basket
    - Swap the prev fruit and cur fruit basket
    - Reset the consecutively picked fruit count to 1
    - Increment the collected fruit count
- Case 3: The fruit matches neither of the fruits in the baskets
    - The current fruit basket becoems the previous fruit basket
    - The new fruit becomes the current fruit basket
    - Update the highest collected count if needed
    - The collected fruit count becomes consecutively picked fruit count + 1
    - Reset the consecutively picked fruit count to 1
At the end, check whether the last collected batch is the highest


Runtime: O(N) where N is length of fruits list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        curFruit = -1
        consecutiveCount = 0
        prevFruit = -1
        collectedFruits = 0

        for fruit in fruits:
            if curFruit == -1 or fruit == curFruit:
                curFruit = fruit
                consecutiveCount += 1
                collectedFruits += 1
            elif prevFruit == -1 or fruit == prevFruit:
                prevFruit = curFruit
                curFruit = fruit
                consecutiveCount = 1
                collectedFruits += 1
            else:
                prevFruit = curFruit
                curFruit = fruit
                ans = max(ans, collectedFruits)
                collectedFruits = consecutiveCount + 1
                consecutiveCount = 1

        ans = max(ans, collectedFruits)
        return ans
