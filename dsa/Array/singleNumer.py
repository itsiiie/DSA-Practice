# 136. Single Number
# Brute Force Method o(n^2)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if  nums.count(num)==1:
                return num


# XOR Method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR each number
        return result



