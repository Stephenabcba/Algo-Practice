// leetcode problem # 1647. Minimum Deletions to Make Character Frequencies Unique

/*
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.


Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
*/


/*
My solution: iteratively delete letters until the string is "good"

oringinal plan was to utilize a heap to slowly delete values until all are unique.
leetcode's related topics of "greedy" and "sorting" inspired improvement (implemented)

idea:
1. find the frequency of each letter in the input string
2. sort the frequencies from largest to smallest
3. once step 1 and 2 is done:
    - if f[x+1] is larger than or equal to f[x], f[x+1] conflicts with f[y] where y < x
        - since the array was sorted before step 3, f[x+1] cannot be greater than f[x] if there were no conflicts
        - f[x+1] must be reduced
        - the first available frequency is f[x] - 1
            - delete letters from f[x+1] until it reaches f[x]-1
                - the amount deleted is f[x+1] - f[x] + 1
                - f[x+1] becomes f[x] - 1
        ** edge case: f[x+1] can only be reduced to a minimum of 0
            - once f[x+1] reaches 0, the corresponding letter no longer affects whether the string is "good"

Runtime: O(N + K * log K) where N is the length of the input string, and K is 26.
- if N is larger (up to 10^5), it will be the most expensive part of the operations
- if N is smaller than 26, then the sorting will be the most expensive operation
Space: O(K) where K is 26.
- the frequency array requires 26 spaces for each lowercase English letter
*/

/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function (s) {
    // initialize the frequencies array
    let frequencies = []
    for (let i = 0; i < 26; i += 1) {
        frequencies.push(0)
    }

    // find the frequency of each character
    for (let letter of s) {
        frequencies[letter.charCodeAt(0) - "a".charCodeAt(0)] += 1
    }

    // sort the frequencies from the largest to the smallest
    frequencies.sort((a, b) => b - a)

    let deleteCount = 0

    // as the frequencies array is sorted, if the array is not in strictly decreasing (f[x] > f[x+n]), letters need to be deleted.
    // as noted by leetcode in example 3, letters with frequencies of 0 are ignored in determination of a "good" string.
    for (let i = 0; i < 25; i += 1) {
        if (frequencies[i] <= frequencies[i + 1]) {
            if (frequencies[i + 1] > frequencies[i + 1] - frequencies[i] + 1) {
                deleteCount += frequencies[i + 1] - frequencies[i] + 1
                frequencies[i + 1] = frequencies[i] - 1
            } else {
                deleteCount += frequencies[i + 1]
                frequencies[i + 1] = 0
            }

        }
    }

    return deleteCount
};