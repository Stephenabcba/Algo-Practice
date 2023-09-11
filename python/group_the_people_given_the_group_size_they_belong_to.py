# leetcode problem # 1282. Group the People Given the Group Size They Belong To

"""
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

Example 1:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

Constraints:
groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""

"""
My solution: Use a dictionary to keep track of groups

Observation: it doesn't matter which group a person is placed in as long as the group size is correct
-> It could be convenient to fill a group with the first person that needs the specific group size

A dictionary is used for grouping people
- the key is the group size, and the value is the index of the people placed in that group
- if the group is full, transfer the group to the answer list and make a new group

Logic:
1. Initialize the output list and the dictionary for grouping people
2. iterate through each person
- place the person in the correct group based on their group size
- move full groups to the output
3. return the completed output list
- as the problem states that there will always be a solution, there is no need to check if the
dictionary is empty

Runtime: O(N) where N is the length of the input list groupSizes
Space: O(N)
"""

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []

        workingGroups = {}

        for idx, groupSize in enumerate(groupSizes):
            workingGroups[groupSize] = workingGroups.get(groupSize, [])
            workingGroups[groupSize].append(idx)
            if len(workingGroups[groupSize]) == groupSize:
                ans.append(workingGroups[groupSize])
                workingGroups[groupSize] = []

        return ans