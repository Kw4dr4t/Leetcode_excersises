"""
Given a sorted array nums, remove the duplicates in-place such
that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means
a modification to the input array will be known to the caller as well.
"""


class Solution:
    def removeDuplicates(self, nums: int) -> int:
        next_new = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[next_new] = nums[i]
                next_new += 1
        return next_new
