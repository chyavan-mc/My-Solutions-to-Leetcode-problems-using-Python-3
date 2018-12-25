class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums2=[]
        nums2+=nums
        for item in range(len(nums)):
            nums[(item+k)%len(nums)]=nums2[item]