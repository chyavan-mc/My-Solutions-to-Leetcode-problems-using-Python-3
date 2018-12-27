class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.EqStr(s)==self.EqStr(t)
            
    def EqStr(self,s):
        dictA = {}
        strA = ""
        if len(s)==0:
            return strA
        dictA[s[0]] = 0
        i=1
        j=1
        while i<len(s):
            if s[i] in dictA.keys():
                pass
            else:
                dictA[s[i]]=j
                j+=1
            i+=1
        
        for item in s:
            strA+=str(dictA[item])
        return strA