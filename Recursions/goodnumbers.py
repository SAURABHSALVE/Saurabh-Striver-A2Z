class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        
        # Calculate how many even and odd indices we have
        # Example n=5: even_pos=3 (0,2,4), odd_pos=2 (1,3)
        even_pos = (n + 1) // 2
        odd_pos = n // 2
        
        # Calculate (5^even_pos) % MOD
        # We use pow(a, b, m) because it is highly optimized O(log n)
        first_part = pow(5, even_pos, MOD)
        
        # Calculate (4^odd_pos) % MOD
        second_part = pow(4, odd_pos, MOD)
        
        # Total = (5^even_pos * 4^odd_pos) % MOD
        return (first_part * second_part) % MOD

# Example usage
if __name__ == "__main__":          
    solution = Solution()
    n = 4
    result = solution.countGoodNumbers(n)
    print(f"Number of good numbers of length {n}: {result}")