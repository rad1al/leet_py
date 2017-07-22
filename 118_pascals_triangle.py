class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        results = [[1]]
        if numRows <= 0:
            return []
        i = 1
        while i < numRows:
            results.append(self.overlap(results[-1]))
            i += 1
        return results

    def overlap(self, row):
        row1 = row + [0]
        row2 = row1[::-1]
        return [row1[i] + row2[i] for i, item in enumerate(row1)]
