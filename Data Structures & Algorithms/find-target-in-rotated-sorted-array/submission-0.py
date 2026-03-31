class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:        # ✅ check first
                return mid
            
            # Left Half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:   # ✅ < not <=
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1                          # ✅ outside the while loop