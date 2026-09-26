class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        """
        Do not return anything, modify nums in-place instead.
        """

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1