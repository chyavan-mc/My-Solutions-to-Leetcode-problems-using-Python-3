class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        valset = set(deck)
        valdict = {}
        for item in valset:
            valdict[item] = deck.count(item)
        numlist = list(valdict.values())
        return self.hcf(numlist)>=2
    
    def hcfnum(self, x,y):
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf
            
    def hcf(self,lis):
        hcf = lis[0]
        for i in range(len(lis)-1):
            if self.hcfnum(lis[i],lis[i+1]) < hcf:
                hcf = self.hcfnum(lis[i],lis[i+1])
        return hcf