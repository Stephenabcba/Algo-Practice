# leetcode problem # 621. Task Scheduler

"""
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. 
Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.


Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done,
so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 10^4
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""

"""
My solution: Space out the most frequent tasks

Main problem complication: Cooling time (n)
- with a cooling time of 0, the tasks can be arranged in any order without conflict
    - the minimum number of intervals is the number of tasks in this case
        -> this is also the minimum number for scheduling tasks if there are no idle cycles
- if cooling time is greater than 0, there may be idle cycles, where no tasks are done in a cycle
due to all tasks being in cooling time
    - however, depending on the tasks and cooling time, it is sometimes also possible to schedule without any idle cycles

Intuition: To minimize the number of idle cycles, schedule the most frequent tasks as soon as their cooling times are over
- The remaining tasks can be filled into any empty cycles in between the cooling times
- If there are no empty cycles, tasks can be inserted anywhere in the schedule, delaying the already scheduled tasks
    - the cooling time only restricts the minimum intervals between identical tasks, and does not impose any requirements
    on the maximum interval
- The final answer is the maximum of the following two values
    1. The total number of tasks 
        - the tasks are scheduled without any empty cycles
    2. The number of intervals required to schedule the more frequest tasks
        - empty cycles exist in the schedule

Runtime: O(M) where M is the length of tasks list
Space: O(1), memory usage does not depend on input
- although the program does use extra space, the most space used is constrained by the
number of types of tasks, which is 26 in this case
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = defaultdict(int)
        for task in tasks:
            taskCount[task] += 1

        counts = list(taskCount.values())
        counts.sort(reverse=True)

        highest = counts[0]
        highestCount = 1
        idx = 1
        while idx < len(counts) and counts[idx] == highest:
            idx += 1
            highestCount += 1

        spacedTask = (n + 1) * (highest - 1) + highestCount
        return max(len(tasks), spacedTask)
