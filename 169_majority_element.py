class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = dict()
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        max_ = max(dct.values())
        for key in dct:
            if dct[key] == max_:
                return key

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) solution. Boyer–Moore majority vote algorithm
        highest = nums[0]
        count = 1
        for i in xrange(1, len(nums)):
            if count == 0:
                count += 1
                highest = nums[i]
            elif highest == nums[i]:
                count += 1
            else:
                count -= 1
        return highest