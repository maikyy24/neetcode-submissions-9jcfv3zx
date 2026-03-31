"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      oldToNone = { None : None}
      current = head
      #create map that stores the LinkedList
      while current:
        copy = Node(current.val)
        oldToNone[current] = copy
        current = current.next

      current = head
      #Since each list in the map has a val and a random we just grab the next one and assign the ponters
      while current:
        copy = oldToNone[current]
        copy.next = oldToNone[current.next]
        copy.random = oldToNone[current.random]
        current = current.next

      return oldToNone[head]

        