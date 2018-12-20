class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = ""
        ascii_list = [*range(65,91),*range(97,123),*range(48,58)]
        for i in s:
            if ord(i) in ascii_list:
                newStr+=i
        newStr=newStr.lower()
        return list(newStr)==list(reversed(list(newStr)))