class Solution:
    def search(self, nums: List[int], target: int) -> int:

        numsort = sorted(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 

            if numsort[m] == target:
                return m
            elif numsort[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
        