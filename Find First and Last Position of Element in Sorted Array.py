class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            i = nums.index(target)
        except:
            return [-1,-1]
        j = list(reversed(nums)).index(target)
        return [i,len(nums)-j-1]