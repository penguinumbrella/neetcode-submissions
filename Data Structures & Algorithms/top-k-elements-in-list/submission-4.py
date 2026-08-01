class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_counter = Counter(nums)

        buckets = [[] for _ in range(len(nums))]

        for num, count in nums_counter.items():
            buckets[count-1].append(num)
        
        print(buckets)

        count = k
        elements = []
        for bucket in buckets[::-1]:
            while bucket: # check if bucket has items
                element = bucket.pop()
                elements.append(element)
                count -= 1
                if count == 0: break
            if count == 0: break


        return elements
        