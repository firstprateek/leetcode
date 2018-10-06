class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = set(range(1, len(nums) + 1))
        
        return list(result - set(nums))
