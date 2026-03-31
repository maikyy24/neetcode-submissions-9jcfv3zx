class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      frequencyS1 = {}
      windowCount = {}
      #adding all the char to frequencyS1
      for c in s1:
        frequencyS1[c] = frequencyS1.get(c , 0) + 1
      left = 0
      for right in range(len(s2)):
        windowCount[s2[right]] = windowCount.get(s2[right], 0) + 1
        if(right >= len(s1)):
          windowCount[s2[left]] -=1
          if windowCount[s2[left]] == 0:
            del windowCount[s2[left]]
          left+=1
        if windowCount == frequencyS1:
          return True
      return False 
      