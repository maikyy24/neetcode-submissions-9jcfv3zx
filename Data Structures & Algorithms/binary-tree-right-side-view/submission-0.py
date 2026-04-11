class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      if root is None: 
        return []
      queue = deque([root])
      result = []
      while queue:
        level_size = len(queue)
        for i in range(level_size):
          currentNode =  queue.popleft()
          if i ==  level_size -1 :
            result.append(currentNode.val)
          if currentNode.left is not None:
            queue.append(currentNode.left)
          if currentNode.right is not None:
            queue.append(currentNode.right)            
      return result 