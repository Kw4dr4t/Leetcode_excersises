"""
Given an array, rotate the array to the right by
k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there
are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums i
        """
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


class Solution2(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
