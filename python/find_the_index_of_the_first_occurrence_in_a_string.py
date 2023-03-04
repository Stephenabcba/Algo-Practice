# leetcode problem # 28. Find the Index of the First Occurrence in a String

"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

"""
My attempt: failed due to excessive runtime

Runtime: O(N * M) where N is the length of the haystack and M is length of the needle
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        needleLength = len(needle)

        haystackIdx = 0
        needleIdx = 0

        while haystackIdx + needleLength <= len(haystack):
            if haystack[haystackIdx + needleIdx] == needle[needleIdx]:
                needleIdx += 1
                if needleIdx == needleLength:
                    return haystackIdx
            else:
                haystackIdx += 1
                needleIdx = 0
        return -1


"""
Solution by leetcode: Rabin-Karp Algorithm (double hash)

Using hashing, the checking process can be reduced to constant time.
- every substring after the first set can be derived 
- the first substring will take O(M) time to hash
    - M must be less than N, as it's impossible to hide a needle larger than the haystack

Spurious hits: Clashing of hashed values, where two different strings have the same hash
- this is undesireable as the alogirthm produces false positives, and must check whether
identical hashes were produced by the same strings

Current hashing method:
1. Mapping Value: Assign a numerical value to each letter (ex: a = 1, b = 2, etc.)
2. Radix: To reduce spurious hits, each value is multiplied by a "radix" value
    - ex: "aba" is hashed as 1 * 26 ^ 0 + 2 * 26 ^ 1 + 3 * 26 ^ 2
    - the radix must be larger than the size of character set to eliminate spurious hits
3. Modulo: Using a radix, the hash value can quickly be too large and overflow; using modulo 
can reduce the value of the number to prevent overflow
    - the moulo value should be a large prime number
    - ex: reducedHash = hash % 509 (the prime should be much larger)
    - however, using a modulo would increase the chance of spurious hits

Improved Hashing method: calculate 2 different hashes
- By changing the three factors above, a second hash can be calculated
- According to leetcode, it can be Mathematically proven that the chance of spurious hits
    can be reduced to 10^-10 using 2 hashes

Runtime: O(N) where N is the 
Space: O(1)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # CONSTANTS
        RADIX_1 = 26
        MOD_1 = 10**9+33
        MAX_WEIGHT_1 = 1
        RADIX_2 = 27
        MOD_2 = 2**31-1
        MAX_WEIGHT_2 = 1

        for _ in range(m):
            MAX_WEIGHT_1 = (MAX_WEIGHT_1 * RADIX_1) % MOD_1
            MAX_WEIGHT_2 = (MAX_WEIGHT_2 * RADIX_2) % MOD_2

        # Function to compute hash_pair of m-String
        def hash_pair(string):
            hash_1 = hash_2 = 0
            factor_1 = factor_2 = 1
            for i in range(m - 1, -1, -1):
                hash_1 += ((ord(string[i]) - 97) * (factor_1)) % MOD_1
                factor_1 = (factor_1 * RADIX_1) % MOD_1
                hash_2 += ((ord(string[i]) - 97) * (factor_2)) % MOD_2
                factor_2 = (factor_2 * RADIX_2) % MOD_2

            return [hash_1 % MOD_1, hash_2 % MOD_2]

        # Compute hash pairs of needle
        hash_needle = hash_pair(needle)

        # Check for each m-substring of haystack, starting at window_start
        for window_start in range(n - m + 1):
            if window_start == 0:
                # Compute hash pairs of the First Substring
                hash_hay = hash_pair(haystack)
            else:
                # Update Hash pairs using Previous using O(1) Value
                hash_hay[0] = (((hash_hay[0] * RADIX_1) % MOD_1
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_1)) % MOD_1
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_1)
                hash_hay[1] = (((hash_hay[1] * RADIX_2) % MOD_2
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_2)) % MOD_2
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_2)

            # If the hash matches, return immediately.
            # Probability of Spurious Hit tends to zero
            if hash_needle == hash_hay:
                return window_start
        return -1
