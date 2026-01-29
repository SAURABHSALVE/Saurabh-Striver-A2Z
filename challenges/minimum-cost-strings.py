class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        # 1. Initialize the cost matrix for 26 lowercase letters
        # We use infinity to represent impossibility initially
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        # Distance to self is always 0
        for i in range(26):
            dist[i][i] = 0
            
        # 2. Populate initial costs from the input arrays
        for o, c, z in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            # Handle duplicate edges by keeping the minimum cost found so far
            dist[u][v] = min(dist[u][v], z)
            
        # 3. Floyd-Warshall Algorithm to find All-Pairs Shortest Path
        # This updates dist[i][j] to be the min cost using intermediate node k
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    # If going from i to k and k to j is cheaper than i directly to j
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        # 4. Calculate total cost for the source string
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            
            current_cost = dist[u][v]
            
            # If the cost is still infinity, transformation is impossible
            if current_cost == inf:
                return -1
            
            total_cost += current_cost
            
        return total_cost

# --- Test Runner Code ---
if __name__ == "__main__":
    solver = Solution()

    # Example 1
    print("--- Example 1 ---")
    s1 = "abcd"
    t1 = "acbe"
    orig1 = ["a","b","c","c","e","d"]
    chng1 = ["b","c","b","e","b","e"]
    cst1 = [2,5,5,1,2,20]
    result1 = solver.minimumCost(s1, t1, orig1, chng1, cst1)
    print(f"Source: {s1}, Target: {t1}")
    print(f"Output: {result1}")
    print(f"Expected: 28\n")

    # Example 2
    print("--- Example 2 ---")
    s2 = "aaaa"
    t2 = "bbbb"
    orig2 = ["a","c"]
    chng2 = ["c","b"]
    cst2 = [1,2]
    result2 = solver.minimumCost(s2, t2, orig2, chng2, cst2)
    print(f"Source: {s2}, Target: {t2}")
    print(f"Output: {result2}")
    print(f"Expected: 12\n")

    # Example 3
    print("--- Example 3 ---")
    s3 = "abcd"
    t3 = "abce"
    orig3 = ["a"]
    chng3 = ["e"]
    cst3 = [10000]
    result3 = solver.minimumCost(s3, t3, orig3, chng3, cst3)
    print(f"Source: {s3}, Target: {t3}")
    print(f"Output: {result3}")
    print(f"Expected: -1\n")