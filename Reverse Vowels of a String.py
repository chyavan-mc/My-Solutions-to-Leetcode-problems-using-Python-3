class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        newlis = []
        vowel = ('a','e','i','o','u','A','E','I','O','U')
        for item in s:
            if item in vowel:
                newlis.append(item)
        
        for i in range(len(s)):
            if s[i] in vowel:
                s = s[:i] + newlis[-1] + s[i+1:]
                del newlis[-1]
        return s