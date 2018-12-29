class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        self.dic = {}
        i=97
        for item in order:
            self.dic[item] = chr(i)
            i+=1
        
        for i in range(len(words)):
            words[i]=self.intEq(words[i])
        
        if words == sorted(words):
            return True
        return False
    
    def intEq(self, string):
        newStr=""
        for item in string:
            newStr += self.dic[item]
        return newStr