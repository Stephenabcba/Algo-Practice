# leetcode problem # 997. Find the Town Judge

"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""

"""
My solution: Use dictionary and list to organize trust relations

Keep track of who trusts a person
- This can be done with a dictionary
    - The key is the person who is trusted
    - The value is the list of people who trust the person

Keep track of whether a person trusts someone
- This can be done with a list
    - If a person trust someone, their value in the list is 1
    - If a person doesn't trust anyone, their value in the list is 0

Using the information above, the judge can be found in linear time
- look for a person whom everyone else trusts
    - if the person trusts someone, there is no judge in this town
        - everybody else already trust someone, and the person also trusts someone
            -> everybody in the town trusts someone, which violates the requirement that
            the judge doesn't trust anyone
    - if the person doesn't trust anyone, the person is the judge
- if the person doesn't exist, there is no judge in this town

Edge Case: if there's only one person in the town, that person must be the town judge

Runtime: O(M + N) where N is the number of people, and M is length of trust list
Space: O(M + N) where N is the number of people, and M is length of trust list
* In the worst case, M could be O(N^2)
"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trustDict = {}
        trusting = [0 for _ in range(n + 1)]

        for relation in trust:
            trustDict[relation[1]] = trustDict.get(relation[1], [])
            trustDict[relation[1]].append(relation[0])
            trusting[relation[0]] = 1

        for person in trustDict:
            if len(trustDict[person]) == n - 1:
                if trusting[person]:
                    return -1
                else:
                    return person

        return -1


"""
Improvement:
As problem boundaries ensure unique trust pairs, it is only necessary to
keep track of how many people trusts a person, rather than who trusts the
person
-> The dictionary only needs to hold the count rather than a list of people

Runtime: O(M + N) where N is the number of people, and M is length of trust list
Space: O(N) where N is the number of people
"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trustDict = {}
        trusting = [0 for _ in range(n + 1)]

        for relation in trust:
            trustDict[relation[1]] = trustDict.get(relation[1], 0) + 1
            trusting[relation[0]] = 1

        for person in trustDict:
            if trustDict[person] == n - 1:
                if trusting[person]:
                    return -1
                else:
                    return person

        return -1
