class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1

        max_area = 0
        while low < high:
            area = (high-low) * min(heights[high],heights[low])
            max_area = max(max_area, area)
            if heights[high] <= heights[low]:
                high -= 1
            else:
                low += 1
        return max_area

        