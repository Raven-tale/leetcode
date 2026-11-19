class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        avg = ans = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            avg = avg + nums[i + k - 1] - nums[i - 1]
            if avg > ans:
                ans = avg
        return ans / k

        """
        Careful of indexes
        Was super tired on initial attempt
        """