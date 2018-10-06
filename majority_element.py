class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                
        for key, value in dict.items():
            if value > len(nums) / 2: return key
