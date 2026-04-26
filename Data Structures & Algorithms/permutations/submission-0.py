class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      result = []
      sol = []
      n = len(nums)
      #create boolean for used 
      used = [False] * n
      def backtracking(nums , path , used , result ):
        if len(path) == len(nums):
          result.append(path[:])
          return
        for i in range(len(nums)):
          if used[i]:
            continue #Already in currentPath
          #Choose
          used[i] = True
          path.append(nums[i])
          backtracking(nums , path , used , result)
          path.pop()
          used[i] = False
      backtracking(nums , [] , used , result)
      return result
