class Solution:
    def isValid(self, s: str) -> bool:

        char_map = {
            ')': '(', 
            '}': '{', 
            ']': '['
            }

        stack = []

        for char in s:
            
            if char in char_map:
                if stack:
                    if stack.pop() != char_map[char]: return False
                else: return False
            else:
                stack.append(char)
        
        if not stack: return True
        return False
        