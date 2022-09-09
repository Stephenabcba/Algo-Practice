# leetcode problem # 1996. The Number of Weak Characters in the Game

"""
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.


Example 1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.

Constraints:
2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attacki, defensei <= 10^5
"""


"""
My attempt 1: brute force
compare every character against every other character, if it is strictly weaker, add it to the count
avoid double counting by keeping track of which characters are already classified as weak
Failed due to O(N^2) runtime took too long
"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        isWeak = [False for i in range(len(properties))]
        weakCount = 0
        for characterI in range(len(properties)):
            for characterJ in range(len(properties)):
                if (characterI != characterJ and isWeak[characterJ] == False):
                    if properties[characterI][0] > properties[characterJ][0] and properties[characterI][1] > properties[characterJ][1]:
                        isWeak[characterJ] = True
                        weakCount += 1
        return weakCount


"""
Attempt 2: slight optimization for case with many weak characters and duplicat attacks

By sorting in the reversed order, the characters with the highest attack will be placed first
- in python3, if two characters have the same attack, the character with higher defense will be placed first

By combining sorting with a condition before running the inner loop, some unnecessary loops could be eliminated
- This reduces the likelyhood of running the inner loop for characters with lower attacks, as lower attacks
- The condition also only processes a character with an attack not processed before
    - for characters with the same attack, the inner loop should only need to process for the character with the highest defense
        - under the condition of same attack, if the character with the highest defense cannot eliminate another character, a character with lower defense
            cannot eliminate the character either.

The worst case is still O(N^2) as the nested loops will run every single time if there are no weak characters
The solution did not pass.
"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(reverse=True)
        isWeak = [False for i in range(len(properties))]
        weakCount = 0
        prevAttack = 10000000000
        for characterI in range(len(properties)):
            if (prevAttack != properties[characterI][0] and isWeak[characterI] == False):
                for characterJ in range(len(properties)):
                    if (characterI != characterJ and isWeak[characterJ] == False):
                        if properties[characterI][0] > properties[characterJ][0] and properties[characterI][1] > properties[characterJ][1]:
                            isWeak[characterJ] = True
                            weakCount += 1
            prevAttack = properties[characterI][0]
        return weakCount


"""
Solution by shivrastogi in leetcode discussion (originally written in Java)

1. Sort the array
- the characters are sorted according to their attacks, from the smallest to the largest
- if two characters have the same attack, the character with higher defense comes first
2. process each character from the back to the front
- in this way, the characters with higher attacks are processed first
    - when characters have the same attack, the character lower defense comes first
- keep track of the highest character defense encountered so far (maxDefense)
    - increase maxDefense whenever a character with higher defense is encountered
- due to the way the array is sorted, if a character with a lower defense than maxDefense is encountered,
    the character MUST have a lower attack than the character with maxDefense
    - the character is a weak character.
- if a character has defense greater than or equal to maxDefense, the character CANNOT be a weak character.

Runtime: O(N * logN) where N is the number of characters (length of properties array)
- main runtime is the sorting algorithm, which takes N log N time
- the for loop runs O(N) times.
Space: O(1), the logic does not use any extra space that scales with input
"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        weakCount = 0

        propertiesLength = len(properties)

        maxDef = properties[propertiesLength-1][1]

        for i in range(propertiesLength-2, -1, -1):
            if (properties[i][1] < maxDef):
                weakCount += 1
            else:
                maxDef = properties[i][1]

        return weakCount
