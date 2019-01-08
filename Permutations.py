class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==1:
            return [nums]
        num = set(nums)
        newlis  =[]
        for item in num:
            for it in self.permute(num - {item}):
                newlis.append([item,*it])
        return newlis