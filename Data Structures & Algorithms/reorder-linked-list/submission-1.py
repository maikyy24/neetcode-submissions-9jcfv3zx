# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        #Find the middle point 
        while fast is not None and fast.next is not None: 
          fast = fast.next.next 
          slow = slow.next
        secondHalf = slow.next
        slow.next = None
        #Reverse Second half
        current = secondHalf 
        prev = None
        while current is not None:
          nextNode = current.next
          current.next = prev
          prev = current
          current = nextNode
        #merge the two list
        while prev is not None:
          current = head.next
          nextPrev = prev.next
          head.next = prev
          prev.next = current
          head = current 
          prev = nextPrev
        