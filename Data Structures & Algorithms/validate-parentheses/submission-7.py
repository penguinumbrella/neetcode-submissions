class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ']':'[',')':"("}

        for c in s:
            if c in pairs.values():
                print("c in values")
                stack.append(c)
            elif c in pairs:
                print("c in keys", stack)
                if not stack:
                    return False
                elif stack[-1] != pairs[c]:
                    print(stack[-1], pairs[c])
                    return False
                else:
                    stack.pop(-1)
        return not stack
            
        