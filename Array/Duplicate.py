class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to store unique numbers

        for num in nums:
            if num in seen:
                return True  # If we’ve already seen this number, it's a duplicate
            seen.add(num)  # Otherwise, add it to the set

        return False  # No duplicates found



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)  # Convert list to a set (removes duplicates automatically)
        return len(nums) != len(s)  # If lengths differ, duplicates were present
