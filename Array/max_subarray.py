class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]         # Start with the first element as the max
        current_sum = nums[0]     # Running sum of current subarray

        for i in range(1, len(nums)):
            # If current_sum is negative, it's better to start new subarray from nums[i]
            current_sum = max(nums[i], current_sum + nums[i])

            # Update max_sum if we found a new max
            max_sum = max(max_sum, current_sum)

        return max_sum
