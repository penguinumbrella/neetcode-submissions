class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        charMap = {}

        for c in s:
            if c not in charMap:
                charMap[c] = 0
            charMap[c] += 1
        print(charMap)
        
        for c in t:
            if c not in charMap or charMap[c] == 0:
                return False
            charMap[c] -= 1
        
        return True