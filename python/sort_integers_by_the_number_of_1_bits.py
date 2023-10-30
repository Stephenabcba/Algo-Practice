# leetcode problem # 1356. Sort Integers by The Number of 1 Bits

"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

Example 1:
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:
Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.

Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 10^4
"""

"""
My solution: Sort According to instructions

Using the default sort function in Python, with a custom sorting logic
1. Count the number of 1's in the binary of the number
2. return the number of 1's and the value itself in a tuple
- Python will sorted based on the number of 1's first
- If the number of 1's is identical, then Python will sort based on the value

Runtime: O(N*logN) where N is the length of arr
Space: O(N)
"""

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def comparison(val):
            oneCount = 0

            for digit in bin(val):
                if digit == '1':
                    oneCount += 1

            return (oneCount, val)

        arr.sort(key=comparison)

        return arr