# leetcode problem # 165. Compare Version Numbers

"""
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:
    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.

Example 1:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 2:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Example 3:
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

Constraints:
1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""

"""
My solution: Two pointers

Idea: compare the revisions of the two versions
- the earliest revision difference decides which version is larger
    - ex: 3.1 is larger than 1.5, as 3.1 has a larger value at revision 0
- to find the value of each revision, a two pointer approach can be used
    - parse each character in the version until a "." is reached
        - multiply the value by 10 for each character parsed to get the correct value
    - compare the parsed revision value
        - if any difference is found, return the corresponding value for the larger version
    - if no differences are found for all the revisions, return 0

Runtime: O(M + N) where M and N are lengths of version1 and version2
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1Idx = 0
        ver2Idx = 0

        while ver1Idx < len(version1) or ver2Idx < len(version2):
            ver1Val = 0
            ver2Val = 0
            while ver1Idx < len(version1) and version1[ver1Idx] != ".":
                ver1Val = ver1Val * 10 + int(version1[ver1Idx])
                ver1Idx += 1
            ver1Idx += 1

            while ver2Idx < len(version2) and version2[ver2Idx] != ".":
                ver2Val = ver2Val * 10 + int(version2[ver2Idx])
                ver2Idx += 1
            ver2Idx += 1

            if ver1Val > ver2Val:
                return 1
            elif ver1Val < ver2Val:
                return -1

        return 0
