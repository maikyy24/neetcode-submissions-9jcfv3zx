class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0

        orderedSet = set(nums)
        longest = 0

        for n in orderedSet:   # ← FIXED (use the set, not nums)
            if (n - 1) not in orderedSet:
                currentNumber = n
                length = 1

                while (currentNumber + 1) in orderedSet:
                    currentNumber += 1
                    length += 1

                longest = max(longest, length)

        return longest


        