class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(nlogn) solution because it involves sorting.
        sorted_nums = sorted(nums)
        return sum([sorted_nums[i] for i, item in enumerate(sorted_nums) if i % 2 == 0])

    def arrayPairSum_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) solution using buckets(?).
        array = [0 for x in xrange(20001)]
        for i in xrange(len(nums)):
            array[nums[i]+10000] += 1
        result = 0
        flag = 0
        j = 0
        while j < 20001:
            if array[j] > 0 and flag == 0:
                result = result + j - 10000
                flag = 1
                array[j] -= 1
            elif array[j] > 0 and flag == 1:
                array[j] -= 1
                flag = 0
            else:
                j += 1
        return result

    def arrayPairSum_3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # another O(n) solution using buckets(?).
        exist = [0 for x in xrange(20001)]
        for i in xrange(len(nums)):
            exist[nums[i] + 10000] += 1
        result = 0
        odd = True
        for j in xrange(20001):
            while exist[j] > 0:
                if odd:
                    result += j - 10000
                odd = not odd
                exist[j] -= 1
        return result