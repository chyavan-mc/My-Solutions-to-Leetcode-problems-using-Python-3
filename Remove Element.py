class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            if val in nums:
                ret = nums.index(val)
                nums.pop(ret)
            else:
                return len(nums)
