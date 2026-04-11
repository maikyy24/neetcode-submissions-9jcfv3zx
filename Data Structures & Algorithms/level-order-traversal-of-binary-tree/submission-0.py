class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if root is None:
        return []
      queue = deque([root])
      result = []
      while queue:
        #see how may nodes are on the currentLevel
        level_size = len(queue)
        currentLevel = []
        for i in range(level_size):
          currentNode = queue.popleft()
          currentLevel.append(currentNode.val)
          if currentNode.left is not None:
            queue.append(currentNode.left)
          if currentNode.right is not None:
            queue.append(currentNode.right)
        result.append(currentLevel)
      return result
