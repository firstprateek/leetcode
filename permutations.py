class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_util(choosen = []):
            if len(choosen) == len(nums):
                res.append(list(choosen))
                return
            
            for value in nums:
                if value in choosen:
                    continue
                #choose
                choosen.append(value)
                #explore
                permute_util(choosen)
                #unchoose
                choosen.pop()
        
        res = []
        if not nums:
            return res
        permute_util()
        return res
                