class Solution:
    def removeDuplicates(self, nums):
        dic = {*nums}
        lis = sorted(dic)
        for i in range(0, len(dic)):
            j = nums.index(lis[i])
            nums[i] = nums[j]
        return len(dic)
