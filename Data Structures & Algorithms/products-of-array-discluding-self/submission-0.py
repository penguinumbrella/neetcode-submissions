class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 for _ in range(len(nums))]
        postfix = [0 for _ in range(len(nums))]

        prod1 = 1
        prod2 = 1

        prefix[0] = prod1
        postfix[len(nums) - 1] = prod2

        

        print(prefix)
        for i in range(1, len(nums)):
            prod1 *= nums[i-1]
            prefix[i] = prod1
        
        print(prefix)

        for i in range(len(nums) - 2, -1, -1):
            prod2 *= nums[i+1]
            postfix[i] = prod2
        print(postfix)
        
        final = []
        for i in range(len(nums)):
            final.append(prefix[i] * postfix[i])

        return final