class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=""
        for i in digits:
            num+=str(i)
        a = list(str(int(num)+1))
        for i in range(len(a)):
            a[i]=int(a[i])
        return a