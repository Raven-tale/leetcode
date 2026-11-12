class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            max_area = max(max_area, (height[l] if height[l] < height[r] else height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

"""
Saw motivation by writing the inequality for incrementing
Missed that we greedily move the lower of value l, r
To try and increase the area
Max is slower than if/else comparison
"""