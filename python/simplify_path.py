# leetcode problem # 71. Simplify Path

"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.


Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""

"""
My solution: Stack

Observation:
".." moves up 1 directory, effectively removing the most recent valid directory
-> some directories the absolute path will not be included in
the canonical path

Using a stack, the interaction with ".." can be handled
    - every time a ".." occurs, pop from the stack if possible
    - a list can be used as a stack

Logic:
1. Separate the path based on "/"
    - this can be done with split()
2. iterate through each item separated in step 1
    - ignore empty strings as they are not actual paths
        - the empty strings occur at the start and end, and when there's multiple slashes together
    - skip ".", as it has no effect on the path
    - when ".." occurs, pop from the stack when possible
    - otherwise, add all other paths to the stack
3. combine the stack with "/" between every item, with a "/" at the start
4. return the answer

Runtime: O(N) where N is the length of path
Space: O(N)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split("/"):
            if len(directory) == 0 or directory == ".":
                continue
            elif directory == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(directory)

        ans = "/" + "/".join(stack)
        return ans
