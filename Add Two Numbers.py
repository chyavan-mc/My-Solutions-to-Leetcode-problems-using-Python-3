# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        carry = 0
        while ptr1.next!=None and ptr2.next!=None:
            temp = (ptr1.val+ptr2.val+carry)//10
            ptr1.val=(ptr1.val+ptr2.val+carry)%10
            carry = temp
            ptr1=ptr1.next
            ptr2=ptr2.next
        
        temp = (ptr1.val+ptr2.val+carry)//10
        ptr1.val=(ptr1.val+ptr2.val+carry)%10
        carry = temp
        
        if ptr2.next==None:
            while carry != 0:
                if ptr1.next == None:
                    ptr1.next = ListNode(carry)
                    carry = 0
                else:
                    temp = (ptr1.next.val+carry)//10
                    ptr1.next.val = (ptr1.next.val+carry)%10
                    carry = temp
                    ptr1 = ptr1.next
            return l1
        
        temp = (ptr2.next.val + carry)//10
        ptr1.next = ListNode((ptr2.next.val + carry)%10)
        carry = temp
        ptr1=ptr1.next
        ptr2=ptr2.next
        
        while ptr2.next!=None:
            temp = (ptr2.next.val + carry)//10
            ptr1.next = ListNode((ptr2.next.val + carry)%10)
            carry = temp
            ptr1=ptr1.next
            ptr2=ptr2.next
        if carry!=0:
            ptr1.next = ListNode(carry)
        return l1