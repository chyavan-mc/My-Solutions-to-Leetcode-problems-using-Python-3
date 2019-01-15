class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red= nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        
        for i in range(red):
            nums[i]=0
        for i in range(red,white+red):
            nums[i]=1
        for i in range(white+red,blue+red+white):
            nums[i]=2