# leetcode problem # 1834. Single-Threaded CPU

"""
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the ith task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.


Example 1:
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

Example 2:
Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.

Constraints:
tasks.length == n
1 <= n <= 10^5
1 <= enqueueTimei, processingTimei <= 10^9
"""

"""
My solution: sort then utilize heap

Intuition:
When a task is done, pick the shortest task available.
If there's no tasks available, wait until a task can be queued

Optimization:
- A task is not available until time reaches enqueueTime of the task (t > task[0])
    -> By sorting the tasks list based on enqueueTime first, the list can be processed in 1 pass.
        - to keep track of the original index, the index is attached to each task
- To keep inserting and removing items from a list that needs to remain sorted, a heap can be used
    - removing and inserting take O(logN) each
    - the heap is organized based on the processingTime of each task

Logic:
1. Attach the original index to each task
2. Sort the tasks list based on enqueueTime
3. Iterate through each item in the tasks list
- add all tasks with enqeueTime <= current time into the heap
- if there's tasks in the heap, increment time until the next available enqueueTime and add the tasks again
- pick the task with the lowest processingTime from the heap
    - increase the time to time + processingTime
    - add the index of the task to the answer list
4. Process the remaining items in the heap once all tasks in the list have been added to the heap
5. Return the answer list

Runtime: O(N * logN) where N is the number of tasks
Space: O(N)
"""


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx in range(len(tasks)):
            tasks[idx].append(idx)
        tasks.sort(key=lambda x: x[0])
        idx = 0
        time = 0
        heap = []
        ans = []

        while idx < len(tasks) or len(heap) > 0:
            while idx < len(tasks) and time >= tasks[idx][0]:
                heapq.heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if len(heap) == 0:
                time = tasks[idx][0]
            else:
                curTask = heapq.heappop(heap)
                time += curTask[0]
                print(curTask[1])
                ans.append(curTask[1])

        return ans
