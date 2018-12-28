# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lis = []
        ptr = head
        while(ptr!=None):
            lis.append(ptr.val)
            ptr=ptr.next
        ptr = self.reverseList(head)
        i=0
        while(ptr!=None):
            if(lis[i]!=ptr.val):
                return False
            i+=1
            ptr=ptr.next
        return True
            
            
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