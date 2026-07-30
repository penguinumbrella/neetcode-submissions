class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complements = {}

        for i in range(len(nums)):
            num = nums[i]

            #print(num, complements)
            
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            
            complements[num] = i
        
        return [0,0]
        