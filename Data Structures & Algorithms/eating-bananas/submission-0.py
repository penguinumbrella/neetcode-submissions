class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = list(range(1, max(piles)))

        l, r = 1, max(piles)

        k = 0
        while l <= r:
            m = l + ((r - l) // 2) # this is our k
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h: 
                k = m
                r = m - 1
            else: l = m + 1
        #print(k)
        return k
        