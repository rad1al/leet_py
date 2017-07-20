class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''.join(map(str,nums))
        return max(map(lambda x: sum([int(k) for k in x]), s.split('0')))
                