class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s_ = s.translate(None, string.punctuation)
        exclude = set(string.punctuation)
        s_ = (''.join(ch.lower() for ch in s if ch not in exclude)).replace(' ', '')
        if len(s) == 0:
            return True
        else:
            return s_[::-1] == s_
    
    def isPalindrome_2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

"""
>>> Solution().isPalindrome("A man, a plan, a canal: Panama")
True
>>> Solution().isPalindrome("A man, a plan, a canal: Panam")
False
>>> Solution().isPalindrome("a A a")
True
>>> Solution().isPalindrome("a A b")
"""