# leetcode problem # 2251. Number of Flowers in Full Bloom

"""
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Example 1:
https://assets.leetcode.com/uploads/2022/03/02/ex1new.jpg
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Example 2:
https://assets.leetcode.com/uploads/2022/03/02/ex2new.jpg
Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Constraints:
1 <= flowers.length <= 5 * 10^4
flowers[i].length == 2
1 <= starti <= endi <= 10^9
1 <= people.length <= 5 * 10^4
1 <= people[i] <= 10^9
"""

"""
Solution by leetcode: Binary search

Idea: Perform a binary search for the number of flowers that has started blooming, and perform another binary
search of the number of flowers that has finished blooming at time i
    - i is a time when a person is visiting
-> the number of flowers blooming at time i is the number of blooming flowers - the number of ended flowers
    - repeat the process for each person visiting

Runtime: O((n+m)*logn) where n is the length of flowers list and m is the length of people list
Space: O(n)
"""

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []
        
        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
            
        starts.sort()
        ends.sort()
        ans = []

        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)
        
        return ans