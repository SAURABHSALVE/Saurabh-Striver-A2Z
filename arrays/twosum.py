## optimal solution using hashmap
def twoSum(nums,target):
    hashmap = {}
    n = len(nums)
    for i in range(n):
        if target - nums[i] in hashmap:
            return [hashmap[target - nums[i]],i]
        hashmap[nums[i]] = i
print(twoSum([1,2,3,4],5))
