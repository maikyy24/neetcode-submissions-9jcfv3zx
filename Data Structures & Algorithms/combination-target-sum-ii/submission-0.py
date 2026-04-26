class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      #sort because to skip duplicates
      candidates.sort()
      n = len(candidates)
      result = []
      def backtracking(i , sol , total):
        if total == target:
          result.append(sol[:])
          return
        
        if total > target or i == n:
          return
        #pick the current i
        sol.append(candidates[i])
        backtracking( i + 1  , sol , total + candidates[i])
        sol.pop()
        #don't pick the current i 
        #we have to do a while loop because in that way we skip all the same elements
        while i + 1  < n and candidates[i] == candidates[i+1]:
          i +=  1
        backtracking(i + 1 , sol , total)
      backtracking( 0 , [] , 0)
      return result