class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      left , right = 0 , 0
      maxLength = 0
      charSet = set()
      while right < len(s):
        if s[right] not in charSet:
          charSet.add(s[right])        
          right +=1
          maxLength = max(maxLength , right - left)
        else:
          charSet.remove(s[left])
          left+=1 
      return maxLength
        