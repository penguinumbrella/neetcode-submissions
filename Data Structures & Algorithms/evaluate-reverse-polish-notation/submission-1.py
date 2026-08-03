class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        accepted_ops = ["+", "-", '*', '/']
        nums = []
        ops = []
        for t in tokens:
            if t in accepted_ops:
                num2 = nums.pop()
                num1 = nums.pop()

                if t == "+":
                    nums.append(num1 + num2)
                elif t == '-':
                    nums.append(num1 - num2)
                elif t == '*':
                    nums.append(num1 * num2)
                else:
                    nums.append(int(num1 / num2))

            else:
                nums.append(int(t))
        #print(nums, ops)
        return nums[0]