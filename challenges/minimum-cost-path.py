import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n, edges):
        
        # Build adjacency list with both forward and reverse edges
        adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))      # Forward edge: cost w
            adj[v].append((u, 2 * w))  # Reverse edge: cost 2 * w
        
        # Standard Dijkstra setup
        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)
        
        while pq:
            cost, u = heapq.heappop(pq)
            
            if cost > dist[u]:
                continue
            
            if u == n - 1:
                return cost
            
            for v, w in adj[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
        
        return dist[n-1] if dist[n-1] != INF else -1
    print("Combinations that sum up to", target, "are:", comb)
    for combination in comb:
        print(combination, end=" ") 
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],      
# [1,7],
# [2,6]]
# Explanation: These are the unique combinations whose sum is equal to target.
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [[1,2,2],[5]]
