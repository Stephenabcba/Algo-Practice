# leetcode problem # 692. Top K Frequent Words

"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.


Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:
1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

"""
My solution: Collect counts of each word then sort

Part 1: Finding frequency of each word
- Iterate through each word in words list and insert in a dictionary
- Keep track of frequency of each word with the dictionary

Part 2: Convert to list then sort
- Convert the dictionary to a list of lists, with the inner list keeping holding the key-value of each entry in the form of [word, frequency]
- Sort the list based on frequency and lexicographical order
    - words with higher frequency comes first
    - words with same frequency will be sorted lexicographically

Part 3: Remove frequency component and slice
- As the final answer does not need frequency, create a new list with only the words (maintaining the same order)
- Slice the list to only the first k items

Runtime: O(N * log(N)) where N is the length of words list
- The most time intensive step is sorting
Space: O(N) where N is the length of words list
- Each data structure contains at most N items
- In total, 1 dictionary and 3 lists are used
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = {}
        for word in words:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1

        freqList = []
        for entry in frequencies:
            freqList.append([entry, frequencies[entry]])

        def customCompare(a, b):
            if a[1] > b[1]:
                return -1
            elif a[1] < b[1]:
                return 1
            else:
                for idx in range(min(len(a[0]), len(b[0]))):
                    if a[0][idx] == b[0][idx]:
                        continue
                    if a[0][idx] < b[0][idx]:
                        return -1
                    else:
                        return 1
                return len(a[0]) - len(b[0])

        sortedList = sorted(freqList, key=functools.cmp_to_key(customCompare))
        return [item[0] for item in sortedList][:k]
