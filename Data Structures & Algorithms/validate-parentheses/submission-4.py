class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
                
        for c in s:
            if c in pairs.values():  # opening brackets
                stack.append(c)
            elif c in pairs:  # closing brackets
                if not stack or stack.pop() != pairs[c]:
                    return False
        return not stack
            
        