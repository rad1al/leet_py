class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        sorted_nums = list(reversed(sorted(nums)))
        ranking = {item : str(i+1) for i, item in enumerate(sorted_nums)}
        for k in ranking:
            if ranking[k] == "1":
                ranking[k] = "Gold Medal"
            elif ranking[k] == "2":
                ranking[k] = "Silver Medal"
            elif ranking[k] == "3":
                ranking[k] = "Bronze Medal"
        return [ranking[item] for i, item in enumerate(nums)]
    
    def find_three_highest_values(nums):
        # Probably O(n) complexity.
        v = [float('-Inf'), float('-Inf'), float('-Inf')]
        for i in xrange(len(nums)):
            if nums[i] > v[2]:
                v[2] = nums[i]
            elif nums[i] > v[1] and nums[i] < v[2]:
                v[1] = nums[i]
            elif nums[i] > v[0] and nums[i] < v[1]:
                v[0] = nums[i]
        return v