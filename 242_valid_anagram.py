class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # comparison sorts yield O(nlogn) complexity.
        return sorted(s) == sorted(t)

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # counting elements in each set yields O(n) complexity.
        return collections.Counter(s) == collections.Counter(t)