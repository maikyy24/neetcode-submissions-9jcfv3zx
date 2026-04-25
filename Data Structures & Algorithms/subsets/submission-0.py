class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      # we need to get all the subsets of the array 
      n = len(nums)
      res , sol = [] , []

      def backtracking(i):
        if i == n :
          res.append(sol[:])
          return
        # don't pick the nums[i]
        backtracking(i + 1)

        #Pick nums[i]
        sol.append(nums[i])
        backtracking(i + 1 )
        sol.pop()
        
      backtracking(0)
      return res