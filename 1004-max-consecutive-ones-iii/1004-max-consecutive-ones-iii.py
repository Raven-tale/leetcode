class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1
        return r - l + 1

        """
        Answer is difference between l, r
        When k > 0, increase window
        When k <= 0, slide window
        This one is quite profound
        """

class Incomplete:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
        while k > 0 and r <= len(nums) - 1:
            if nums[r] == 0:
                k -= 1
            r += 1
        while nums[r] == 1:
            r += 1
        r -= 1
        ans = r - l

        """
        Know solution, implementation messy n tricky
        Initial conditions
        Loop sliding window
        """
