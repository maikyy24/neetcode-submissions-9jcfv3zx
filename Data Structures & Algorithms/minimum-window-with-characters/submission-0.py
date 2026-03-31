class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        frequencyT ={}
        #Adding the values to the mapp 
        for c in t:
            frequencyT[c] = frequencyT.get(c ,  0) + 1
        required = len(frequencyT)
        formed = 0
        windowCount = {}
        left = 0
        best = (float('inf') , 0 , 0)
        for right in range(len(s)):
            windowCount[s[right]] = windowCount.get(s[right] , 0) +1
            if s[right] in frequencyT and windowCount[s[right]] == frequencyT[s[right]]:
                formed +=1
            while formed == required:
                if(right - left + 1) < best[0]:
                    best = (right - left + 1 , left , right)
                windowCount[s[left]] -=1
                if s[left] in frequencyT and windowCount[s[left]] < frequencyT[s[left]]:
                    formed -=1
                left +=1
        return "" if best[0] == float('inf') else s[best[1] : best[2] + 1]  