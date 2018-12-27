# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return root
        self.switch(root)
        return root
    
    
    def switch(self, node):
        temp = node.left
        node.left = node.right
        node.right = temp
        
        if(node.left!=None):
            self.switch(node.left)
        if(node.right!=None):
            self.switch(node.right)