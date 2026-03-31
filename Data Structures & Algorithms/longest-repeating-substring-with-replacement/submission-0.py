class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      count = {}
      left = 0 
      maxFreq = 0 
      result = 0
      for right in range(len(s)):
        # 1. Expand the window
        count[s[right]] = count.get(s[right], 0) + 1
        # 2. Update maxFreq
        maxFreq = max(maxFreq, count[s[right]])
        # 3. Shrink if invalid
        if (right - left + 1) - maxFreq > k:
          count[s[left]] -= 1
          left += 1
        # 4. Update result
        result = max(result, right - left + 1)
      return result
        