class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        summ = 0
        nums=sorted(nums)

        for i in range(0,len(nums),2):
            summ += min(nums[i],nums[i+1])

        return summ