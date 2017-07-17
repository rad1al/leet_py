class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        results = list()
        pos_dict = {item : i for i, item in enumerate(nums)}
        for i, i_item in enumerate(findNums):
            count = 0
            for j, j_item in enumerate(nums[pos_dict[i_item]:]):
                if j_item > i_item:
                    results.append(j_item)
                    break
                else:
                    count += 1
            if count == len(nums[pos_dict[i_item]:]):
                results.append(-1)
        return results
                    
    def nextGreaterElement_2(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        results = list()
        pos_dict = {item : None for i, item in enumerate(nums)}
        j = 0
        # k = 0
        while True:
            if len(nums[j:]) == 0:
                break
            s = False
            for k in nums[j+1:]:
                if nums[j] < k:
                    pos_dict[nums[j]] = k
                    s = True
                    break
            if s == False:
                pos_dict[nums[j]] = -1
            j += 1
        results = [pos_dict[x] for x in findNums]
            
        return results

    def nextGreaterElement_3(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n) solution possibly. Dictionary (hash table in python) insertion is O(1) best case, O(n) worst case.
        dct_ = dict()
        stack = list()
        for num in nums:
            while len(stack)!=0 and stack[-1] < num:
                dct_[stack.pop()] = num
            stack.append(num)
        for i in xrange(len(findNums)):
            findNums[i] = self.get_or_default(dct_, findNums[i])
        return findNums
    
    def get_or_default(self, dct_, k):
        try:
            return dct_[k]
        except:
            return -1