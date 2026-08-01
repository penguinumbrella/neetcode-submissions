class Solution:
    def isPalindrome(self, s: str) -> bool:
        sa = "".join([char for char in s if char.isalnum()]).lower()
        #print(sa)
        
        l,r = 0, len(sa) - 1
        while l <= r:
            if sa[l] != sa[r]:
                return False
            l += 1
            r -= 1
        return True