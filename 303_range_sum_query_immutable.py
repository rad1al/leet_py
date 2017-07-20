class NumArray(object):
    # Time complexity : O(n) time per query. Each sumRange query takes O(n) time.
    # Space complexity : O(1). Note that data is a reference to nums and is not a copy of it.
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


class NumArray(object):
    """
    Time complexity : O(1) time per query, O(n^2) time pre-computation. 
    The pre-computation done in the constructor takes O(n^2) time. 
    Each sumRange query's time complexity is O(1) as the hash table's look up operation is constant time.
    Space complexity : O(n^2). The extra space required is O(n^2) as there are nn candidates for both i and j.
    """
    dct = dict()
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # dct = dict()
        for i in xrange(len(nums)):
            total = 0
            for j in xrange(i, len(nums)):
                total += nums[j]
                self.dct[(i, j)] = total
        # self.mapping.
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dct[(i,j)]

class NumArray(object):
    """
    Time complexity: O(1) time per query, 0(n) time pre-computation.
    Since the cumulative sum is cached, each sumRange query can be calculated in O(1) time.
    Space complexity: O(n)
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lst = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            self.lst[i+1] = self.lst[i] + nums[i]
        # self.lst = lst

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.lst[j+1] - self.lst[i]




# NumArray([-8,2,7,-9,2,9]).sumRange(2,4)