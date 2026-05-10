class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Step 1: Reverse the digits of n
        r = int(str(n)[::-1])
        
        # Step 2: Define the range
        lo = min(n, r)
        hi = max(n, r)
        
        # Step 3: Sieve of Eratosthenes up to hi
        if hi < 2:
            return 0
        
        is_prime = [True] * (hi + 1)
        is_prime[0] = is_prime[1] = False
        
        for p in range(2, int(hi**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, hi + 1, p):
                    is_prime[i] = False
        
        # Step 4: Sum primes only within [lo, hi]
        return sum(i for i in range(max(2, lo), hi + 1) if is_prime[i])