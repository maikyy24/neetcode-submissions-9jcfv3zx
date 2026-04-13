# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      count = 0
      def dfs(node , maxSoFar):
        if node is None:
          return 0
        count = 1 if node.val >= maxSoFar else 0
        count += dfs(node.left , max(node.val , maxSoFar))
        count += dfs(node.right , max(node.val , maxSoFar))
        return count
      return dfs(root, root.val)  