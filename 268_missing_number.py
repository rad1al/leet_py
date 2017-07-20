class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums) 
        return ({x for x in xrange(len(nums)+1)} - s).pop()

    def missingNumber_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(1) + O(n) complexity
        gauss_total = (len(nums)*(len(nums)+1))/2
        return gauss_total - sum(nums)

    def missingNumber_3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ((len(nums)*(len(nums)+1)) >> 1) - sum(nums)