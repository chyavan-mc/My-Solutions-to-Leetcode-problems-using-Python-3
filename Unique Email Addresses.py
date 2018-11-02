def index(lis,char):
    for iter in range(len(lis)):
        if(lis[iter]==char):
            return iter
    return -1
    
def count(lis,char):
    count=0
    for iter in range(len(lis)):
        if(lis[iter]==char):
            count+=1
    return count

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        final=[]
        for item in emails:
            atind = index(item,"@")
            lis=list(item[:atind])
            
            if (count(lis,"+")!=0):
                lis = lis[1:index(lis,"+")]
            
            while(count(lis,".")!=0):
                del lis[index(lis,".")]
            
            strlis = "".join(lis)
            final.append(strlis+item[atind:])
        
        return len(set(final))