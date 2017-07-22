class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort nums and compare result to unsorted nums. Find the max and min 
        # index that have a discrepancy and find the difference + 1.
        # Time complexity : O(nlogn) because of sorting.
        # Space complexity : O(n) because we made a copy of the original list.
        
        mismatches = [i for i, item in enumerate(zip(nums, sorted(nums))) if item[0] != item[1]]
        if len(mismatches) == 0:
            return 0
        else:
            return max(mismatches) - min(mismatches) + 1

Solution().findUnsortedSubarray([2,6,4,8,10,9,15]) == 5



