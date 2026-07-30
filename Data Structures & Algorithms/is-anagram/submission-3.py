class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        s_count = Counter(s)
        t_count = Counter(t)
        print(s_count)
        print(t_count)

        for letter in s_count:
            if s_count[letter] != t_count[letter]:
                return False
        return True
        