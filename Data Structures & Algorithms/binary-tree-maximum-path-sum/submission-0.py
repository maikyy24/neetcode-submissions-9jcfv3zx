# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      maxPath = float('-inf')
      def dfs(node):
        nonlocal maxPath
        if node is None:
          return 0
        # we start at the root we need to get the value for the childs
        #we are at the parent calculate the value of the child from the left and right
        leftGain = max(dfs(node.left) , 0)
        rightGain = max(dfs(node.right) , 0)   
        #Calculate the parent value
        parentValue = node.val + leftGain + rightGain
        maxPath = max(parentValue , maxPath) 
        #
        return node.val + max(leftGain , rightGain)
      dfs(root)
      return maxPath

