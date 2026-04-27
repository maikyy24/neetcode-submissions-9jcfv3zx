class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      nums.sort()
      result = []
      def backtracking(i , subset):
        # if we have reach the end of the tree
        if i == len(nums):
          result.append(subset[:])
          return
        # all subsets that include num[i]
        subset.append(nums[i])
        backtracking(i + 1 , subset)
        subset.pop()

        # all subset that don't include num[i]
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
          i+=1
        backtracking(i + 1 , subset)
      backtracking(0 , [])
      return result