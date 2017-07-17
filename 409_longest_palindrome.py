class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = collections.Counter(s).values()
        evens = [x for x in counts if x % 2 == 0]
        odds = sorted([x for x in counts if x % 2 == 1])
        if 1 in odds:
            return 1 + sum(evens) + odds[-1] + [x-1 for x in odds]
        else:
            return sum(evens) + odds[-1] + [x-1 for x in odds]

    def longestPalindrome_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s: # count for each letter, O(n)
            d[c] = d.get(c, 0) + 1
        # subtract the "number of odd values minus 1" or zero from the string length, O(n)
        return len(s) - max(len(tuple(v for v in d.values() if v % 2)) - 1, 0)

assert Solution().longestPalindrome("abccccdd") == 7
assert Solution().longestPalindrome("ccc") == 3