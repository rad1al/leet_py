class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

    class Solution(object):
    def intersection_2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        results = set()
        set1 = set(nums1)
        for item in nums2: 
            if item in set1 and item not in results:
                results.add(item)
        return list(results)