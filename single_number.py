"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""


class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        return xor
