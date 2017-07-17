class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Likely O(n^2) complexity
        while True:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Likely O(n) complexity.       
        nextPos = 0
        for num in nums:
            if num != val:
                nums[nextPos] = num
                nextPos += 1
        return nextPos