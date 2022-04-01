// leetcode problem # 344. Reverse String

/*
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:

1 <= s.length <= 10^5
s[i] is a printable ascii character.
*/

/*
My solution: swapping the front values with the back values
- work outwards in
- Swapping:
    - store one of the variables to a temp variable
    - reassign the the first variable to the second variable
    - reassign the second variable to the temp value
it takes N/2 swaps to completely reverse the string
*/

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
    for (let i = 0; i < s.length / 2; i++) {
        const temp = s[s.length - 1 - i]
        s[s.length - 1 - i] = s[i]
        s[i] = temp
    }
};

/*
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
*/