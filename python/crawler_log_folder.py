# leetcode problem # 1598. Crawler Log Folder

"""
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Example 1:
https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

Example 2:
https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png
Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Example 3:
Input: logs = ["d1/","../","../","../"]
Output: 0

Constraints:
1 <= logs.length <= 10^3
2 <= logs[i].length <= 10
logs[i] contains lowercase English letters, digits, '.', and '/'.
logs[i] follows the format described in the statement.
Folder names consist of lowercase English letters and digits.
"""

"""
My solution: Count the number of open folders

Iteratively process each operation in the log
- if the operation is "../": decrement the folder count
    - if the folder count was already 0, do nothing
- if the operation is "./": do nothing
- if the operation is a folder name: add 1 to the folder count

Runtime: O(N) where N is the length of logs
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folderCount = 0
        for operation in logs:
            if operation == "../":
                if folderCount > 0:
                    folderCount -= 1
            elif operation != "./":
                folderCount += 1
        return folderCount
