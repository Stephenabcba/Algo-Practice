# leetcode problem # 393. UTF-8 Validation

"""
Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.



Example 1:
Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:
Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

Constraints:
1 <= data.length <= 2 * 10^4
0 <= data[i] <= 255
"""

"""
My solution: process byte by byte following the criteria

Reiterating the given criteria:
- The bytes can either be a header byte (first byte in a unicode character) or an info byte (the remaining bytes in a unicode character)
- The number of info bytes depends on the header byte that comes before
    - a header byte in the form of 0xxxxxxx is a 1-byte unicode
        - there are no trailing info bytes before the next header byte
        - this corresponds to all values under 128
    - a header byte in the form of 110xxxxx is a 2-byte unicode
        - 1 info byte comes after
        - this corresponds to values of 224 > byte >= 192
    - a header byte in the form of 1110xxxx is a 3-byte unicode
        - 2 info bytes come after
        - this corresponds to values of 240 > byte >= 224
    - a header byte in the form of 11110xxx is a 4-byte unicode
        - 3 info bytes come after
        - this corresponds to values of 248 > byte >= 240
    - if any other values are encountered when a header byte is expected, input is invalid.
- The format of an info byte must be in the form 10xxxxxx
    - if any other formats are encountered when an info byte is expected, input is invalid

Enforcing the criteria:
- keep track of the number of info bytes expected in iteration
    - if there is any remaining expected info bytes, the next byte must be an info byte
    - info bytes can be checked by bit shifting the values 6 places to the right
        - if the value is 2, the byte is an info byte
        - otherwise, the byte is not an info byte, return False
    - decrement the count each iteration
- when there are no remaining expected info bytes, the next byte is a header byte
    - check the four cases using the ranges specified above
    - update the number of info bytes expected after
        - a 1-byte has 0 trailing info bytes
        - a 2-byte has 1 trailing info byte
        - a 3-byte has 2 trailing info bytes
        - a 4-byte has 3 trailing info bytes
    - if the byte does not fit any of the four cases, it is invalid
        - return False
When iteration is over, there should be no remaining expected info bytes
    - if the expected value is not 0, return False
    - otherwise, return True

Runtime: O(N) where N is the number of bytes in the data list
Space: O(1), memory usage does not scale with input size.
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        infoBytes = 0

        for byte in data:
            if infoBytes > 0:
                if byte >> 6 != 2:
                    return False
                infoBytes -= 1
            else:
                if byte < 128:
                    infoBytes = 0
                elif 224 > byte >= 192:
                    infoBytes = 1
                elif 240 > byte >= 224:
                    infoBytes = 2
                elif 248 > byte >= 240:
                    infoBytes = 3
                else:
                    return False
        return infoBytes == 0
