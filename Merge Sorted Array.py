class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums3 = sorted(nums1[:m]+nums2[:n])
        for i in range(m+n):
            if(i < len(nums1)):
                nums1[i]=nums3[i]
            else:
                nums1.append(nums3[i])
        while len(nums1)<m+n:
            del nums1[-1]