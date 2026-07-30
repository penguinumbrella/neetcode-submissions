class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1: return False
        curr_s = [s[0]]
        print(curr_s)

        for c in s[1:]:
            print(c)
            print("curr_s", curr_s)
            if c == "{" or c == "(" or c == "[":
                curr_s.append(c)
            else:
                if not curr_s: return False
                else:
                    if c == "}":
                        if curr_s.pop() != "{":
                            return False
                    elif c == "]":
                        if curr_s.pop() != "[":
                            return False
                    elif c == ")":
                        if curr_s.pop() != "(":
                            return False
        if len(curr_s) == 0:
            return True
        return False
            
        