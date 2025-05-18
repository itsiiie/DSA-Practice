# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}      # Dictionary to store frequency of nums1
        result = []

        # Step 1: Count elements in nums1
        for num in nums1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Loop through nums2 and collect common elements
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1  # Decrease count to avoid duplicate matching

        return result
