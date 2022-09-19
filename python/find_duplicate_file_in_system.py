# leetcode problem # 609. Find Duplicate File in System

"""
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Example 2:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Constraints:
1 <= paths.length <= 2 * 10^4
1 <= paths[i].length <= 3000
1 <= sum(paths[i].length) <= 5 * 10^5
paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.

Follow up:
Imagine you are given a real file system, how will you search files? DFS or BFS?
If the file content is very large (GB level), how will you modify your solution?
If you can only read the file by 1kb each time, how will you modify your solution?
What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
How to make sure the duplicated files you find are not false positive?
"""

"""
My solution: Split twice and save data with dictionary

Pseudo Code:
1. Separate the files+content from each other and from the directory
- this could be done by using the split() function on each string with space (" ") as separator.
2. For each files+content format, separate the file name from the content
- this could also be done using split(), this time using the left parenthesis ("(") as the separator
    - remove the right parenthesis (")") from the content
3. Store the content with the full file path
- The data can be stored in a dictionary
    - the keys are the contents as string
    - the values are the concatenation of folder name + file name
4. If any content is repeated, return each cluster as a list
- check each key-value pair in the dictionary, if more than 1 entry is linked to the key, the content is duplicated
    - add it to the answer.

Runtime: O(N * M) where N is the number of distinct folders (len(paths)) and M is the length of each folder string (len(paths[i]))
- Each string in paths is split by the number of spaces, which repeats the operation N times
- the minimum length of a filename + content format is 7 characters (empty content), so there could be roughly M / 7 files
    - this is still O(M)
- in parallel to the operation above, each file + content format is split again, resulting in O(M) operation
    - although the strings are split by each file, in total each letter in the string is only processed once in this operation.
- Thus, the total runtime is N * (M + M), which is O(N * M)
Space: O(L) where L is the sum of length of all strings saved in paths list
- in the worst case, there are no duplicate files, and the dictionary has to save each file path as its own entry.

"""


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        organizedSystems = {}
        for directory in paths:
            # split the string into the folder name, and the filename + content format
            separated = directory.split(" ")
            folderName = separated[0]
            for file in range(1, len(separated)):
                fileName, content = separated[file].split("(")
                content = content[0:-1]
                if content not in organizedSystems:
                    organizedSystems[content] = []
                organizedSystems[content].append(folderName + "/" + fileName)

        ans = []

        for cluster in organizedSystems.values():
            # only add the cluster of paths if the data occurred more than once
            if (len(cluster) > 1):
                ans.append(cluster)

        return ans
