# O(n) space solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        return True if arr == arr[::-1] else False

# O(1) space with keeping input intact

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = fast = head
        rev = None
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        head = slow
        if fast:
            slow = slow.next
            
        isPal = True
        while rev:
            if rev.val != slow.val:
                isPal = False
            
            rev, head, head.next, slow = rev.next, rev, head, slow.next
        
        return isPal