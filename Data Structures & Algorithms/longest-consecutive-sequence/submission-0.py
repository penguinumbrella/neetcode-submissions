class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest = 0
        for n in numset:
            if (n - 1) not in numset: # this is the start of a sequence!
                length = 1
                while n + length in numset:
                    length += 1
                longest = max(length, longest)
        
        return longest

        