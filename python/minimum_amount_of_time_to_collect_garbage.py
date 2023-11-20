# leetcode problem # 2391. Minimum Amount of Time to Collect Garbage

"""
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.

Example 1:
Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
Output: 21
Explanation:
The paper garbage truck:
1. Travels from house 0 to house 1
2. Collects the paper garbage at house 1
3. Travels from house 1 to house 2
4. Collects the paper garbage at house 2
Altogether, it takes 8 minutes to pick up all the paper garbage.
The glass garbage truck:
1. Collects the glass garbage at house 0
2. Travels from house 0 to house 1
3. Travels from house 1 to house 2
4. Collects the glass garbage at house 2
5. Travels from house 2 to house 3
6. Collects the glass garbage at house 3
Altogether, it takes 13 minutes to pick up all the glass garbage.
Since there is no metal garbage, we do not need to consider the metal garbage truck.
Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.

Example 2:
Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
Output: 37
Explanation:
The metal garbage truck takes 7 minutes to pick up all the metal garbage.
The paper garbage truck takes 15 minutes to pick up all the paper garbage.
The glass garbage truck takes 15 minutes to pick up all the glass garbage.
It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.


Constraints:
2 <= garbage.length <= 10^5
garbage[i] consists of only the letters 'M', 'P', and 'G'.
1 <= garbage[i].length <= 10
travel.length == garbage.length - 1
1 <= travel[i] <= 100
"""

"""
My solution: Count the route of each truck separately

Observations:
1. The trucks only need to travel to the last house that has trash of the corresponding time
2. Even if they don't collect anything, the trucks still need to travel through every house before the last house they collect from
3. As only 1 truck can be operated at 1 given time, the time taken for each truck is added for the total time

Logic:
1. Iterate through each house
    - keep track of the total time taken to reach the house (from the start)
    - count the trash based on its category
    - if a trash category is present in this house, update the longest time travelled for the category
    - add the number of trash to the total trash amount collected for the category
2. Return the total time given after adding everything together

Runtime: O(N) where N is the number houses to collect from
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        metalRoute = 0
        metalPickup = 0
        paperRoute = 0
        paperPickup = 0
        glassRoute = 0
        glassPickup = 0

        travelTime = 0

        for house in range(len(garbage)):
            if house > 0:
                travelTime += travel[house - 1]

            curMetal = 0
            curPaper = 0
            curGlass = 0

            for trash in garbage[house]:
                if trash == "M":
                    curMetal += 1
                elif trash == "P":
                    curPaper += 1
                elif trash == "G":
                    curGlass += 1

            if curMetal > 0:
                metalRoute = travelTime
                metalPickup += curMetal
            if curPaper > 0:
                paperRoute = travelTime
                paperPickup += curPaper
            if curGlass > 0:
                glassRoute = travelTime
                glassPickup += curGlass

        return metalRoute + metalPickup + paperRoute + paperPickup + glassRoute + glassPickup
