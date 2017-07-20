class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        return max(s[-1]*s[-2]*s[-3], s[-1]*s[0]*s[1])

        # Folliwng solution is probably O(n) complexity.
        # Not sure why it isn't working...
        # max1 = float('-Inf')
        # max2 = float('-Inf')
        # max3 = float('-Inf')
        # min1 = float('Inf')
        # min2 = float('Inf')
        # for num in nums:
        #     if num > max1:
        #         max3 = max2
        #         max2 = max1
        #         max1 = num
        #     elif num > max2:
        #         max3 = max2
        #         max2 = num
        #     elif num > max3:
        #         max3 = num
        # if num < min1:
        #     min2 = min1
        #     min1 = num
        # elif num < min2:
        #     min2 = num
        # return max(max1*max2*max3, max1*min1*min2)


Solution().maximumProduct([-1,-2,-4,5,6,8])