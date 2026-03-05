## optimal solution using hashmap
def twoSum(nums, target):
    hashset = {}
    n = len(nums)
    for i in range(n):
        if target - nums[i] in hashset:
            return [hashset[target - nums[i]],i]
        hashset[nums[i]] = i
    return False