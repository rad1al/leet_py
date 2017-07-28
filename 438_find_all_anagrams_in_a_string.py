class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # O(n) solution using a sliding window and Counter from collections.
        # With each step through s, lower count of oldest letter in window and 
        # increase count of newest letter.
        lst = list()
        p_count = collections.Counter(p)
        window = collections.Counter(s[:len(p)-1])
        for i in xrange(len(p)-1, len(s)):
            window_start_index = i-len(p)+1
            window[s[i]] += 1
            if window == p_count:
                lst.append(window_start_index)
            window[s[window_start_index]] -= 1
            if window[s[window_start_index]] == 0:
                del window[s[window_start_index]]
        return lst