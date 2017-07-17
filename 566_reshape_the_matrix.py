class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        vals = reduce(lambda x,y : x+y, nums)
        return [vals[i*c:(i+1)*c] for i in xrange(len(vals)/c)]
        