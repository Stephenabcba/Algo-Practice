# leetcode problem # 2306. Naming a Company


"""
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

 

Example 1:

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.
 

Constraints:

2 <= ideas.length <= 5 * 10^4
1 <= ideas[i].length <= 10
ideas[i] consists of lowercase English letters.
All the strings in ideas are unique.
"""

"""
My Attempt: Failed due to runtime exceeded

Group all words by their initials, as words that have the same initial will not create new
word pairs.

If a pair of words create a new word pair, two word pairs are created, as word1 in the first
pair can become word2 in the second pair and vice versa.

Runtime: O(N^2 * M) where N is number of strings and M is length of each string
Space: O(N * M)
"""


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0
        ideaSet = set(ideas)

        ideaAlphabetical = [[] for letter in range(26)]
        for idea in ideas:
            ideaAlphabetical[ord(idea[0]) - ord("a")].append(idea)

        for idea1Initial in range(26):
            if len(ideaAlphabetical[idea1Initial]) > 0:
                for idea1Word in ideaAlphabetical[idea1Initial]:
                    for idea2Initial in range(idea1Initial + 1, 26):
                        if len(ideaAlphabetical[idea2Initial]) > 0:
                            for idea2Word in ideaAlphabetical[idea2Initial]:
                                newWord1 = idea2Word[0] + idea1Word[1:]
                                newWord2 = idea1Word[0] + idea2Word[1:]
                                if newWord1 in ideaSet:
                                    break
                                if newWord2 not in ideaSet:
                                    ans += 2
        return ans


"""
Solution By leetcode: Group words by their initials

Skip all mutual words

Runtime: O(N * M) where N is the number of strings, and m is length of the strings
Space: O(N * M)
"""


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Group idea by their initials.
        initial_groups = [set() for _ in range(26)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])

        answer = 0
        # Calculate number of valid names from every pair of groups.
        for i in range(25):
            for j in range(i + 1, 26):
                # Get the number of mutual suffixes.
                num_of_mutual = len(initial_groups[i] & initial_groups[j])

                # Valid names are only from distinct suffixes in both groups.
                # Since we can swap a with b and swap b with a to create two valid names, multiple answer by 2.
                answer += 2 * \
                    (len(initial_groups[i]) - num_of_mutual) * \
                    (len(initial_groups[j]) - num_of_mutual)

        return answer
