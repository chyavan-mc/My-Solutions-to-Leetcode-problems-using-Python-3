# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverse(root, root.val)
    
    
    def traverse(self,node,value):
        if node == None:
            return True
        return self.traverse(node.left, value) and self.traverse(node.right, value) and node.val==value