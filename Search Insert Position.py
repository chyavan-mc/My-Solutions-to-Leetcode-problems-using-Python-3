class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)

        except:
            lis = sorted(nums + [target])
            return lis.index(target)

