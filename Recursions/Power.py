class Solution(object):
    def myPow(self, x, n):
        if n ==0:
            return 1
        if n <0:
            x = 1/x
            n = -n
            
            
        return self.fastPow(x, n)

    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        
        # Recursive call: Divide the problem in half
        half = self.fastPow(x, n // 2)
        
        # If n is even: x^8 = x^4 * x^4
        if n % 2 == 0:
            return half * half
        # If n is odd: x^9 = x^4 * x^4 * x
        else:
            return half * half * x
# Example usage
if __name__ == "__main__":        
    solution = Solution()
    x = 2.0
    n = 10
    result = solution.myPow(x, n)
    print(f"{x}^{n} = {result}")