# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(minSoFar , maxSofar , node):
          if node is None:
            return True
          if node.val <= minSoFar or node.val >= maxSofar:
            return False
          return dfs(minSoFar , node.val , node.left) and dfs(node.val , maxSofar , node.right) 
                  
        return dfs(float('-inf') , float('inf') , root)