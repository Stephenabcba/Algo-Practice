// leetcode problem # 820. Short Encoding of Words

/*
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.


Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].


Constraints:
1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
*/

/*
My solution:
A brute force approach is highly inefficent, but it will perform the task.
- create a boolean array of whether a word is in the encoding list
    - the lenth of the boolean array is the length of the words array
    - initially, all values in the array are set to true; all words start in the encoding list
- iterate through each word and compare to all words with higher indices
    - if the current word can encode another word, the other word is taken off the encoding list (false in boolean array)
    - if another word can encode the current word, the current word is taken off the encoding list (false in boolean array)
    - if a word is not on the encoding list, it does not need to be processed.
- at the end of iterations, the words corresponding to "true" in the boolean array are encoded.
    - sum of lengths of every encoded word + number of encoded words is the answer.

Runtime: O(k*N^2) where k is the maximum length of each word, and N is length of words array. The main logic is a nested for-loop nesting a while loop
Space: O(N), where N is length of words array. Main memory usage is the boolean array.
*/

/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding = function (words) {
    const encoded = []
    for (let i = 0; i < words.length; i++) {
        encoded.push(true)
    }

    for (let i = 0; i < words.length; i++) {
        if (encoded[i] == false) {
            continue
        }
        for (let j = i + 1; j < words.length; j++) {
            if (encoded[j] == false) {
                continue
            }
            let shorterWord = words[i]
            let longerWord = words[j]
            let iShorter = true
            if (shorterWord.length > longerWord.length) {
                shorterWord = words[j]
                longerWord = words[i]
                iShorter = false
            }

            let shorterWordIdx = shorterWord.length - 1
            let longerWordIdx = longerWord.length - 1
            while (shorterWordIdx >= 0) {
                if (shorterWord[shorterWordIdx] != longerWord[longerWordIdx]) {
                    break
                }
                shorterWordIdx--
                longerWordIdx--
            }
            if (shorterWordIdx < 0) {
                if (iShorter) {
                    encoded[i] = false
                } else {
                    encoded[j] = false
                }
            }
        }
    }
    let answer = 0
    for (let i = 0; i < words.length; i++) {
        if (encoded[i]) {
            answer += 1 + words[i].length
        }
    }

    return answer
};

/*
Solution from leetcode: Trie (solution originally written in Java)
Basic idea: remove words that are suffixes of another word in the list

A trie builds a prefix tree by definition
By inserting the words backwards, the trie becomes a suffix tree

When all words from the words array has been inserted into the trie, all leaf nodes (nodes with no children) are words that are not suffixes of another word.
The answer is sum of all lengths of these words + count of these words.
*/
/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding2 = function (words) {


    class TrieNode {
        constructor() {
            this.children = []
            for (let i = 0; i < 26; i++) {
                this.children.push(null)
            }
            this.count = 0
        }

        get(c) {
            if (this.children[c.charCodeAt(0) - 'a'.charCodeAt(0)] == null) {
                this.children[c.charCodeAt(0) - 'a'.charCodeAt(0)] = new TrieNode()
                this.count++
            }
            return this.children[c.charCodeAt(0) - 'a'.charCodeAt(0)]
        }
    }

    const trie = new TrieNode()
    const nodes = new Map()

    for (let i = 0; i < words.length; i++) {
        let word = words[i]
        let cur = trie
        for (let j = word.length - 1; j >= 0; j--) {
            cur = cur.get(word[j])
        }
        nodes.set(cur, i)
    }

    let ans = 0

    nodes.forEach((idx, node) => {
        if (node.count == 0) {
            ans += words[idx].length + 1
        }
    })

    return ans
};



const testWords1 = ["time", "me", "bell"] // expected: 10
const testWords2 = ["t"] // expected: 2
const testWords3 = ["time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell", "time", "me", "bell"] // expected: 10

console.log("my solution")
console.log(minimumLengthEncoding(testWords1))
console.log(minimumLengthEncoding(testWords2))
console.log(minimumLengthEncoding(testWords3))

console.log("leetcode solution")
console.log(minimumLengthEncoding2(testWords1))
console.log(minimumLengthEncoding2(testWords2))
console.log(minimumLengthEncoding2(testWords3))