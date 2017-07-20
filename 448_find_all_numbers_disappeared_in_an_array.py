class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list({x for x in xrange(1,len(nums)+1)} - set(nums))
