class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=""
        if not strs:
            return prefix
        for i in range(len(strs[0])):
            char=strs[0][i]
            for string in strs:
              if i>=len(string) or string[i]!=char:
                  return prefix
            prefix+=char
        return prefix
