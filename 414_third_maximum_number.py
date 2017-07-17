class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        if len(num_set) < 3:
            return max(num_set)
        num_set.remove(max(num_set))
        num_set.remove(max(num_set))
        return max(num_set)

    def thirdMax_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:   
                    v = [num, v[0], v[1]]
                elif num > v[1]: 
                    v = [v[0], num, v[1]]
                elif num > v[2]: 
                    v = [v[0], v[1], num]
        if float('-inf') in v:
            return max(nums) 
        else: 
            return v[2]
