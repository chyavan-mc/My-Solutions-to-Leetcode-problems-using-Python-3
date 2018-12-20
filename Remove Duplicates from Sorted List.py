# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr=head
        if ptr==None:
            return head
        
        while (ptr.next!=None):
            if(ptr.val==ptr.next.val):
                if(ptr.next.next==None):
                    ptr.next=None
                else:
                    ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return head