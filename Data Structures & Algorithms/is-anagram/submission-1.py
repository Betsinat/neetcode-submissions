class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      hs = {}
      ht = {}
      if len(s) != len(t):
        return False
      for c in s:
        if c in hs:
            hs[c] += 1
        else:
            hs[c] = 1
      for c in t:
        if c in ht:
            ht[c] += 1
        else:
            ht[c] = 1
      for c in s:
        if c not in t:
            return False
        if hs[c] != ht[c]:
            return False
      return True

      
      
        