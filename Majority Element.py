class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sett = set(nums)
        dic = {}
        for i in sett:
            dic[i]=nums.count(i)
        for i in dic:
            if dic[i]>(len(nums)/2):
                return i