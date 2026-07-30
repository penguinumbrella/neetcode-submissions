class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_new = "".join([char.lower() for char in s if char.isalnum()])
        #print(s_new)

        for l in range(len(s_new)):
            r = len(s_new) - l - 1
            #print(s_new[l], s_new[r])
            if s_new[l] != s_new[r]: return False

        return True