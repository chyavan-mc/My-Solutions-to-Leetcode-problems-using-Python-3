# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        cpt,ptr=head,head
        ptr=ptr.next
        head.next = None
        
        while(ptr!=None):
            head=ptr
            ptr=ptr.next
            head.next=cpt
            cpt=head
        return head