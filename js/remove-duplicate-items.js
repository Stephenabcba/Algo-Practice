// leetcode problem #316. Remove Duplicate Letters
/*
Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

lexicographical order: comparing 2 strings character by character
1. starting from the first letter, compare the strings character by character
2. if the letters at the current position are the same, compare the next character
3. if the letters at the current position are different, the string with the higher character code value is larger
    - i.e. z>y>x...>a
**NOTE** the comparison does not change the position of any values in the string
- "cba" cannot be rearranged to "abc"
- thus, strategic removal of letters for this algorithm is required

examples:
abc < cba
explanation: "a"<"c" in the first position

abcz < abde
explanation: 
both strings are the same for "a" and "b", but "c" < "d" in the 3rd position
the comparison is based on the first different value, and thus "z" and "e" do not get compared


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
*/

/*
Solution taken from discussion by brainstormer26 (original written in python)
idea:
- letters with higher character values should be as far back as possible
- ideally, in a string that contains all 26 English letters, the returned string should be in alphabetical order
    - "a" should be in the front and "z" should be in the back
    - this leads to the smallest lexicographical order for the English alphabet
    - however, this may not be possible depending on the letters in the input string

implementation:
1. preprocessing: iterate through the string the first time to find the last occurrance index of all letters that exists in the string
    - this information is stored in a dictionary / object for easy retrieval
    - by definition, the last occurred index denotes that there are no additional instances in the letter later in the string
        -ex: in a string of length 1000, if "a" has its last occurance index at 10, "a" must not exist from index 11 to index 1000
2. iterate through the string again to build a stack that will eventually hold all letters to be returned in correct order
    - the stack is stored as an array in this implementation
    - 2.1 if the letter is not in the stack, push it to the stack
        - 2.1.1 before pushing the letter, pop all letters that have larger values than the current letter AND have a duplicate letter later in the string
            - popping the letter essentially moves the popped letter later in the stack, which lowers the result string's lexicographical value
            - only pop from the top of the stack, as some letters could be "locked" in place
            - if a letter with larger value has already reached its last occurance, all previous letters in the stack are "locked in place"
                - it is impossible to move the letter at is last occurance further back in the string without changing the order of the string
            - the last occurance index of any letter in the string can be checked with the dictionary created in (1)
            - if the current index is smaller than the last occurance index for the popped letter, 
                there is at least one duplicate of the letter later in the string
                (guaranteed to have at least the letter saved at the last occurance index)
    - 2.2 if the letter is in the stack, we do not need to do anything
        - if the letter should've been pushed to the stack now, its value should've been removed from the stack in (2.1.1) during earlier iterations
3. return the string built from the stack array
    - each letter occurs exactly once, and the stack array holds the letters in the lowest lexicographical order

as the implementation does not depend on the characters in the string, it will work for any string with any character set
- the comparison uses default javascript comparison for each character

Runtime: O(N * m) or O(N)
    N is the length of the string
        the function iterates through the entire string twice in parallel levels
    m is the the number of all possible letters, 26 in this case for all lower case letters in the English alphabet
        in the worst case, the stack will build up to 25 letters and then pop everything
        as m is a constant number, it could be omitted removed from the big O notation
*/

/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function (s) {
    const lastOccurrance = {}
    for (let i = 0; i < s.length; i++) {
        const letter = s.charAt(i)
        lastOccurrance[letter] = [i]
    }
    const stack = []
    for (let i = 0; i < s.length; i++) {
        if (!stack.includes(s.charAt(i))) {
            while (stack && stack[stack.length - 1] > s.charAt(i) && lastOccurrance[stack[stack.length - 1]] > i) {
                stack.pop()
            }
            stack.push(s.charAt(i))
        }
    }
    return stack.join("")
};

const s1 = "bcabc"
const output1 = "abc"
const s2 = "cbacdcbc"
const output2 = "acdb"
const s3 = "abcdefghijklmnopqrstuvwxyz"

console.log(removeDuplicateLetters(s2))