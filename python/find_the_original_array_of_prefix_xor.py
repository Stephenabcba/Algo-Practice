# leetcode problem # 2433. Find The Original Array of Prefix Xor

"""
You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

Example 1:
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

Example 2:
Input: pref = [13]
Output: [13]
Explanation: We have pref[0] = arr[0] = 13.

Constraints:
1 <= pref.length <= 10^5
0 <= pref[i] <= 10^6
"""

"""
My solution: Use properties of XOR

Properties of XOR:
1. XOR is commutative.
This means, a^b = b^a.

2. XOR is associative.
This means, a^(b^c) = (a^b)^c = (a^c)^b.

3. XOR is self-inverse.
This means, any number XOR'ed with itself evaluates to 0.
a^a = 0.

4. 0 is the identity element for XOR.
This means, any number XOR'ed with 0 remains unchanged.
a^0 = a.

Observation: pref[i] can be written as pref[i - 1] ^ arr[i]
- this is true for all 1 <= i < len(pref)
    - arr[0] is pref[0]
- The expression is equivalent to the following lines (using properties of XOR)
pref[i]               = pref[i - 1] ^ arr[i]
pref[i] ^ pref[i - 1] = pref[i - 1] ^ (pref[i - 1] ^ arr[i])      (XOR on both sides)
pref[i] ^ pref[i - 1] = (pref[i - 1] ^ pref[i - 1]) ^ arr[i]      (Associative property)
pref[i] ^ pref[i - 1] = (0) ^ arr[i]                              (Self-inverse)
pref[i] ^ pref[i - 1] = arr[i]                                    (0 is identity for XOR)

using the relation above, arr[i] can be found for all i given pref

Runtime: O(N) where N is the length of pref list
Space: O(1), memory usage is constant excluding the memory for output
"""

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]

        for idx in range(1, len(pref)):
            new = pref[idx - 1] ^ pref[idx]
            arr.append(new)

        return arr