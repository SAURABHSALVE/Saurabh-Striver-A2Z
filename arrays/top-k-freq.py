class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] = hashmap[nums[i]]+1
            else:
                hashmap[nums[i]] = 1 
        ## convert this into the list 

        freq_list = []
        for num in hashmap:
            freq_list.append([hashmap[num],num])
        ## sort in desecending order 
        freq_list.sort(reverse = True)
        ## now append the second position values in result 
        res = []
        for i in range(k):
            res.append(freq_list[i][1])
        return res 