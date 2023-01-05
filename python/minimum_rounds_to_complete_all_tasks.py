# leetcode problem # 2244. Minimum Rounds to Complete All Tasks

"""
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

 

Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
 

Constraints:

1 <= tasks.length <= 10^5
1 <= tasks[i] <= 10^9
"""

"""
My solution: Use Dictionary

Using a dictionary, tasks with the same difficulties can be grouped together.

For each difficulty, if there's only 1 task with that difficulty, the task can't be done. Return -1
Otherwise:
- Group as many tasks into groups of 3 as possible, and the last 0-2 groups will be groups of 2
    - after making groups of 3:
        if remainder is 0: there's no groups of 2
        if remainder is 2: there's 1 group of 2
        if remainder is 1: there's 2 groups of 2; break up a group of 3 so there's 4 remaining, and make 2 groups of 2

Count the number of groups (rounds) made, and return the number if there wasn't a task that cannot be done.

Runtime: O(N) where N is the number of tasks
Space: O(N)

"""


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        difficulties = {}
        for task in tasks:
            difficulties[task] = difficulties.get(task, 0) + 1

        rounds = 0

        for difficulty in difficulties.values():
            group3 = difficulty // 3
            difficulty = difficulty % 3
            group2 = difficulty // 2
            difficulty = difficulty % 2
            if difficulty == 1:
                if group3 == 0:
                    return -1
                else:
                    group3 -= 1
                    group2 += 2
            rounds += group3 + group2

        return rounds
