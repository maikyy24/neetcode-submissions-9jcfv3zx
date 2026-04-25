class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      n = len(candidates)
      result  = []
      sol = []
      def backtracking(i , target):
        if target == 0 :
          result.append(sol[:])
          return
        if i == n or target < 0:
          return
        # don't pick the current i 
        backtracking(i + 1 ,  target)
        # pick the current i
        sol.append(candidates[i])
        backtracking(i ,  target - candidates[i])
        sol.pop()
      backtracking(0 , target)
      return result