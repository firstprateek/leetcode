# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def reverseList(self, head, previous = None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastNode = None
        def reverse(head, previous):
            nonlocal lastNode
            
            if head == None:
                lastNode = previous
                return
        
            reverse(head.next, head)
        
            head.next = previous
        
        reverse(head, previous)
                
        return lastNode
