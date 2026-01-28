import heapq

class Solution(object):
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        
        # dist[i][j][t] = min cost to reach (i,j) using t teleports
        dist = [[[INF]*(k+1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0
        
        # Sort cells by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        
        # Pointer per teleport layer
        ptr = [0] * (k+1)
        
        heap = [(0, 0, 0, 0)]  # (cost, i, j, teleports_used)
        
        while heap:
            cost, i, j, t = heapq.heappop(heap)
            
            if cost > dist[i][j][t]:
                continue
            
            if (i, j) == (m-1, n-1):
                return cost
            
            # Normal moves
            for ni, nj in [(i, j+1), (i+1, j)]:
                if 0 <= ni < m and 0 <= nj < n:
                    new_cost = cost + grid[ni][nj]
                    if new_cost < dist[ni][nj][t]:
                        dist[ni][nj][t] = new_cost
                        heapq.heappush(heap, (new_cost, ni, nj, t))
            
            # Teleport
            if t < k:
                while ptr[t] < m*n and cells[ptr[t]][0] <= grid[i][j]:
                    _, ni, nj = cells[ptr[t]]
                    if cost < dist[ni][nj][t+1]:
                        dist[ni][nj][t+1] = cost
                        heapq.heappush(heap, (cost, ni, nj, t+1))
                    ptr[t] += 1
        
        return -1


# -------------------------------
# Testing in VS Code
# -------------------------------

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    grid1 = [[1,3,3],[2,5,4],[4,3,5]]
    k1 = 2
    print("Test Case 1 Output:", sol.minCost(grid1, k1))
    print("Expected: 7")
    print()

    # Test Case 2
    grid2 = [[1,2],[2,3],[3,4]]
    k2 = 1
    print("Test Case 2 Output:", sol.minCost(grid2, k2))
    print("Expected: 9")
    print()

    # Custom Test Case 3
    grid3 = [[5,4,3],[6,1,2],[7,8,1]]
    k3 = 1
    print("Test Case 3 Output:", sol.minCost(grid3, k3))
