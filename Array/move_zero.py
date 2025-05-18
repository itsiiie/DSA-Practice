class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0  # This tells where to put the next non-zero number

        # Step 1: Move all non-zero numbers to the front
        for num in nums:
            if num != 0:
                nums[pos] = num  # Put non-zero at current position
                pos += 1         # Move to next position

        # Step 2: Fill the rest of the list with 0s
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
