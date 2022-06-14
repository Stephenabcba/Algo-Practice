// leetcode problem # 1332. Remove Palindromic Subsequences

/*
You are given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string if it is generated by deleting some characters of a given string without changing its order. Note that a subsequence does not necessarily need to be contiguous.

A string is called palindrome if is one that reads the same backward as well as forward.


Constraints:

1 <= s.length <= 1000
s[i] is either 'a' or 'b'.
*/

/*
My solution: check if S is palindrome.

As letters in s can only be 'a's or 'b's, any string s containing a mix of 'a's and 'b's can be split into 2 subsequences, one containing all the 'a's in s and the other containing all the 'b's in s.
    - the 2 subsequences are always palindromes
    - if s only contains 'a' or s only contains 'b', there will be only one subsequence created

As the problem does not ask for which specific palindromic subsequences are removed, the algorithm does not process that information
- if the problem does ask for one example set of subsequences:
    - return s if s is palindrome
    - return 2 subsequences, one containing all 'a's and the other containing all 'b's.

In the best case scenario, the string s is a palindrome; the minimum steps required is 1.
Otherwise, the minimum steps required is 2.

Checking palindrome algorithm:
- utilizing the definition of palindromes, a simple loop can be created checking whether the 1st and last, the 2nd and second last... etc. match.
    - if all the pairs checked matched, s is a palindrome.
    - otherwise, s is not a palindrome.
    - if s has an odd number of letters, the center letter will always match with itself, and thus does not need to be checked.

Runtime: O(N), where N is the length of string s. The check palindrome algorithm runs in linear time.
Space: O(1), the space does not scale with input size.
*/


/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function (s) {
    // in the worst case, s can be split into 2 subsequences of all 'a's and all 'b's
    // both of these subsequences are always palindromes
    // Thus, the maximum minimum number of steps to take is 2, when s is not a palindrome.

    let i = 0
    let j = s.length - 1
    while (i < j) {
        if (s[i] != s[j]) { // s is not a palindrome.
            return 2
        }
        i++
        j--
    }
    // s is a palindrome.
    return 1
};

/*
Example 1:
Input: s = "ababa"
Output: 1
Explanation: s is already a palindrome, so its entirety can be removed in a single step.

Example 2:
Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "". 
Remove palindromic subsequence "a" then "bb".

Example 3:
Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "". 
Remove palindromic subsequence "baab" then "b".
*/