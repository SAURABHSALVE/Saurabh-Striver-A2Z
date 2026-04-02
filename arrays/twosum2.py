class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1,right+1]
            if sum > target:
                right -=1 
            else:
                left +=1

        








        # hashset = {}
        # for i in range(len(numbers)):  
        #     need = target - numbers[i]
        #     if need in hashset:
        #         return [hashset[need]+1,i+1]
        #     hashset[numbers[i]] = i
        





## examples
solution = Solution()
print(solution.twoSum([2,7,11,15],9))  # Output: [1, 2]
print(solution.twoSum([2,3,4],6))  # Output: [1, 3]
print(solution.twoSum([-1,0],-1))  # Output: [1, 2]
