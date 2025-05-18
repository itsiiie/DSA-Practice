class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # This will store numbers we've seen so far, with their index

        # Loop through each number in the list along with its index
        for i, num in enumerate(nums):
            c = target - num  # c is the number we need to find to reach the target

            # If we already saw the number we need, return the pair of indices
            if c in map:
                return [map[c], i]

            # If not, store the current number with its index for later use
            map[num] = i
