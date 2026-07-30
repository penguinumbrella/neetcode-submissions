class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seenMap = []
        for n in nums:
            if n in seenMap:
                return True
            seenMap.append(n)
        return False