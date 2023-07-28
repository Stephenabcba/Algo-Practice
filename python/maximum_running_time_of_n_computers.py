# leetcode problem # 2141. Maximum Running Time of N Computers

"""
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

Example 1:
https://assets.leetcode.com/uploads/2022/01/06/example1-fit.png
Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:
https://assets.leetcode.com/uploads/2022/01/06/example2.png
Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation: 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.

Constraints:
1 <= n <= batteries.length <= 10^5
1 <= batteries[i] <= 10^9
"""

"""
Solution by leetcode: binary search


Using binary search, eliminate half of the solution space every iteration
- to confirm whether the target cycles can be reached, iterate through each battery:
    1. if the battery has lower capacity than the target, the entire battery can be used
    2. if the battery has higher capacity than the target, only the target number of cycles can
        be used.
        * In X cycles, a single battery can only be used X times
            - for each cycle, the battery can only be placed in 1 computer
                - 1 use/cycle * X cycles = X uses
- if the target can be reached, the maximum running time is higher than or equal to the target
- otherwise, the maximum running time is lower than the target


Runtime: O(M * logK) where M is the number of batteries and K is the maximum cycles given the total battery capacity
- K is the sum of the total battery capacity divided by the number of computers N
Space: O(1)
"""

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n
        
        while left < right:
            target = right - (right - left) // 2
            
            extra = 0
            for power in batteries:
                extra += min(power, target)
            
            if extra // n >= target:
                left = target
            else:
                right = target - 1
        
        return left