# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      size = 1
      dummy = head
      #Getting the size
      while dummy.next is not None:
        size +=1
        dummy = dummy.next
      #if negative means the head is the value to remove
      if (size - n ) -1 < 0 :
        return head.next
      current = head
      for i in range((size - n - 1)):
        current = current.next
      current.next = current.next.next
      return head

        