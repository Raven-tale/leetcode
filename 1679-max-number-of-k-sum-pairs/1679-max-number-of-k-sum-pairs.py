class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, ops, r = 0, 0, len(nums) - 1
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == k:
                del nums[l]
                del nums[r - 1]
                r -= 2
                ops += 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return ops

        """
        Think solution is sort then two pointers
        Does work but is too slow...
        No need to reset l and r entirely cos sorted
        Barely works haha
        """
