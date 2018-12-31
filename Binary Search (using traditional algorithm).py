class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums)-1
        start = 0
        while end >= start:
            mid = (end+start)//2
            if nums[mid]>target:
                end = mid - 1
            elif nums[mid]<target:
                start = mid + 1
            else:
                return mid
        return -1