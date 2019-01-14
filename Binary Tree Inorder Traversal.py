# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.lis = []
        if root==None:
            return []
        self.lis += self.inorderTraversal(root.left)
        self.lis += [root.val]
        self.lis += self.inorderTraversal(root.right)
        return self.lis
        