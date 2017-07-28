class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = {i for i in xrange(1, len(nums)+1)}
        n = set(nums)
        missing = (s - n).pop()
        
        return [sum(nums)+missing-sum(s), missing]
        