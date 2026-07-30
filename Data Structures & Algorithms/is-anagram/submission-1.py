class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
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
        
        for c in charMap:
            if charMap[c] != 0: return False
        return True