class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      carry = 0
      head = None
      tail = None
      while l1 or l2 or carry:
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        currentInt = sum % 10
        carry = sum // 10
        if head is  None:
          head = ListNode(currentInt)
          tail = head
        else:
          tail.next = ListNode(currentInt)
          tail = tail.next
        if l1:
          l1 = l1.next
        if l2:
          l2 = l2.next
          
      return head 