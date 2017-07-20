class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Probably should try to implement binary search.
        # This approach is O(n) instead of O(logn)

        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        for i, item in enumerate(nums):
            if item == target:
                return i
            if item < target < nums[i+1]:
                return i+1