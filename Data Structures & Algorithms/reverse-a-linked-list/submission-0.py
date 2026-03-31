class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      current = head 
      prev = None 
      if current is None:
        return None
      while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
      return prev
        