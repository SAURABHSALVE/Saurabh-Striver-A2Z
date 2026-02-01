class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters)

        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[left % len(letters)]


# ---------- Testing ----------
sol = Solution()

print(sol.nextGreatestLetter(["c","f","j"], "a"))  # Expected: c
print(sol.nextGreatestLetter(["c","f","j"], "c"))  # Expected: f
print(sol.nextGreatestLetter(["x","x","y","y"], "z"))  # Expected: x
