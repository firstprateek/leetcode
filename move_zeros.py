from collections import deque

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        que = deque()
        
        for index, num in enumerate(nums):
            if num == 0:
                que.append(index)
                continue
            
            if que and que[0] < index:
                pos0 = que.popleft()
                nums[pos0], nums[index] = nums[index], nums[pos0]
                que.append(index)
