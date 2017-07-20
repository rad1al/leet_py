class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Need a better solution.
        if k == 0:
            pass
        else:
            for i in xrange(k):
                nums.insert(0, nums.pop())
        