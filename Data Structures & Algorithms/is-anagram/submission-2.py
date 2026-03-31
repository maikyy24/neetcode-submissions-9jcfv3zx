class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequencyMap1 = {}
        frenquencyMap2 = {}
        for ch in s:
            frequencyMap1[ch] = frequencyMap1.get(ch, 0)+1
        for ch in t:
            frenquencyMap2[ch] = frenquencyMap2.get(ch, 0)+1
        return frenquencyMap2 == frequencyMap1

