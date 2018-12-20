# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ptr = root
        if(ptr==None):
            return True
        
        return self.CheckSym(ptr,ptr)
    
    
    def CheckSym(self,x,y):
        if(x==None and y==None):
            return True
        elif(x!=None and y!=None):
            if(x.val==y.val):
                return self.CheckSym(x.left,y.right) and self.CheckSym(x.right,y.left)
        return False