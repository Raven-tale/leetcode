class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            hl, hr = height[l], height[r]
            area = (hl if hl < hr else hr) * (r - l)
            if area > max_area:
                max_area = area
            if hl < hr:
                while l < r and height[l] <= hl:
                    l += 1
            else:
                while l < r and height[r] <= hr:
                    r -= 1
        return max_area

"""
Saw motivation by writing the inequality for incrementing
Missed that we greedily move the lower of value l, r
To try and increase the area

Optimisations:
Max on 2 vars is slower than if/else comparison marginally
Keep incrementing to reduce outer loop if conditions met
"""