class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        print(l, r)

        k = 0
        while l <= r:
            m = l + (r - l) // 2

            hours = sum(math.ceil(pile / m) for pile in piles)

            if hours <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
        