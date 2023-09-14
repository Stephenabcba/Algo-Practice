# leetcode problem # 332. Reconstruct Itinerary

"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""

"""
Solution in leetcode solutions by user vanAmsen: DFS
https://leetcode.com/problems/reconstruct-itinerary/solutions/4041944/95-76-dfs-recursive-iterative/?envType=daily-question&envId=2023-09-14

Logic:
1. Convert the list of tickets into a graph
    - the structure of the graph is saved in a dictionary of lists
        - by using a defaultdict, there's is no need for creating entries manually
        - the key in the dictionary is a starting location for a ticket
        - the value in the dictionary is a list of all destination locations from the given starting location
            - the list is sorted in reverse lexical order, such that the smallest lexical destination is placed last
            - the list will be used like a stack, which accesses the last item first before the other items
            -> the combination of the two properties above ensures that the resulting itinerary has the smallest lexical order
2. Perform DFS starting from JFK
    - recursively traverse through the graph, popping a destination from the list each time
3. Backtrack at the end to trace the path traversed
    - the traced path would be in reversed order from the last destination to the first
4. Reverse the backtracked path to get the itinerary
Runtime: O(N * logN)
Space: O(N)
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)
        
        dfs("JFK")
        
        return itinerary[::-1]