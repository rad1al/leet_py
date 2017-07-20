class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splt = s.split()
        if len(splt) == 0:
            return 0
        return len(splt[-1])

    def lengthOfLastWord_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        tail = len(s)-1
        while 0 <= tail and s[tail] == ' ':
            tail -= 1
        while 0 <= tail and s[tail] != ' ':
            result += 1
            tail -= 1
        return result

                